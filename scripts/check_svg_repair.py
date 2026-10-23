#!/usr/bin/env python3
"""Check repair operations against named SVG path endpoints in local MCF diagrams.

Supports the separated --shaft/--head convention, M/L/Z paths, rectangular
node shapes, explicitly bound junctions, and declared native-text attachment
ports (not glyph-ink contact). Returns 0 pass, 1 invalid plan/
input, 2 unassessed geometry. Scientific validity still needs source review
and actual viewing. No figure is edited; --out must be a new file.
"""
import argparse
import collections
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

TOL = 0.25
NS = "{http://www.w3.org/2000/svg}"
TOKEN = re.compile(r"[MmLlZz]|[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?")
NUMBER = re.compile(r"[-+]?(?:\d*\.\d+|\d+\.?\d*)(?:[eE][-+]?\d+)?\Z")


class InvalidInput(ValueError):
    pass


class Unassessed(ValueError):
    pass


def guard(path):
    path = Path(path).absolute()
    for item in (path, *path.parents):
        if item.is_symlink():
            raise InvalidInput("Symlink path refused: " + str(item))
    return path


def read(path):
    path = guard(path)
    data = path.read_bytes()
    return data, {"path": str(path), "bytes": len(data),
                  "sha256": hashlib.sha256(data).hexdigest()}


def read_json(path):
    data, pin = read(path)
    try:
        value = json.loads(data)
    except (UnicodeError, ValueError) as error:
        raise InvalidInput("Invalid JSON: " + str(path)) from error
    if not isinstance(value, dict):
        raise InvalidInput("JSON root must be an object: " + str(path))
    return value, pin


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def distance_to_polyline(point, vertices):
    distances = []
    for a, b in zip(vertices, vertices[1:]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        fraction = ((point[0] - a[0]) * dx + (point[1] - a[1]) * dy) / (dx * dx + dy * dy)
        fraction = min(1.0, max(0.0, fraction))
        distances.append(dist(point, [a[0] + fraction * dx, a[1] + fraction * dy]))
    return min(distances)


def path_points(raw):
    """Strict absolute, single-subpath M/L/Z reader; never approximate curves."""
    if not isinstance(raw, str) or not raw:
        raise Unassessed("Missing path data")
    tokens = TOKEN.findall(raw)
    if re.sub(TOKEN, "", raw).strip(" ,\t\r\n"):
        raise Unassessed("Unsupported SVG path command or syntax")
    points, closed, pos, command = [], False, 0, None
    while pos < len(tokens):
        token = tokens[pos]
        if token in ("M", "L", "Z", "m", "l", "z"):
            pos += 1
            if token in ("m", "l"):
                raise Unassessed("Relative paths are unsupported")
            if token in ("Z", "z"):
                if closed or not points or pos != len(tokens):
                    raise Unassessed("Multiple or malformed closed subpaths")
                closed = True
                break
            if token == "M" and points:
                raise Unassessed("Multiple subpaths are unsupported")
            if token == "L" and not points:
                raise Unassessed("Path must start with M")
            command = token
        if command is None or pos + 1 >= len(tokens):
            raise Unassessed("Malformed M/L coordinate pair")
        if not NUMBER.fullmatch(tokens[pos]) or not NUMBER.fullmatch(tokens[pos + 1]):
            raise Unassessed("Malformed M/L coordinate pair")
        pair = [float(tokens[pos]), float(tokens[pos + 1])]
        if not all(math.isfinite(v) for v in pair):
            raise Unassessed("Nonfinite SVG coordinate")
        points.append(pair)
        pos += 2
        command = "L"
    if not points:
        raise Unassessed("Empty path")
    return points, closed


def visible_chain(element, parents, allow_zero_text_rotation=False):
    for item in (element, *parents[element]):
        if item.get("transform"):
            # Matplotlib emits rotate(-0 x y) on native text. Accept only this
            # identity on the selected text itself, never on an ancestor.
            rotation = re.fullmatch(r"rotate\(\s*([^ ,]+)[ ,]+([^ ,]+)[ ,]+([^ ,]+)\s*\)", item.get("transform"))
            identity = False
            if allow_zero_text_rotation and item is element and item.tag == NS + "text" and rotation:
                try:
                    angle, x, y = map(float, rotation.groups())
                    identity = angle == 0 and x == float(item.get("x", "")) and y == float(item.get("y", ""))
                except ValueError:
                    pass
            if not identity:
                raise Unassessed("Transformed geometry is unsupported")
        if item.get("class"):
            raise Unassessed("Class-styled geometry needs separate rendering review")
        style = {k.strip(): v.strip() for k, v in
                 (piece.split(":", 1) for piece in item.get("style", "").split(";")
                  if ":" in piece)}
        style.update({k: item.get(k) for k in ("display", "visibility", "opacity")
                      if item.get(k) is not None})
        if style.get("display") == "none" or style.get("visibility") in ("hidden", "collapse"):
            raise Unassessed("Hidden selected geometry")
        if "opacity" in style:
            try:
                if float(style["opacity"]) <= 0:
                    raise Unassessed("Invisible selected geometry")
            except ValueError as error:
                raise Unassessed("Unresolved opacity") from error


def single_path(ident, index, parents):
    if ident not in index:
        raise Unassessed("Missing named geometry: " + ident)
    group = index[ident]
    visible_chain(group, parents)
    paths = [element for element in group.iter() if element.tag == NS + "path"]
    if len(paths) != 1 or any(element.tag == NS + "use" for element in group.iter()):
        raise Unassessed("Expected one native path for " + ident)
    path = paths[0]
    visible_chain(path, parents)
    return path_points(path.get("d"))


def rectangle(ident, index, parents):
    points, closed = single_path(ident, index, parents)
    if closed and len(points) == 5 and dist(points[0], points[-1]) < 1e-9:
        points = points[:-1]
    if not closed or len(points) != 4:
        raise Unassessed("Node is not a four-corner closed rectangle: " + ident)
    xs, ys = [p[0] for p in points], [p[1] for p in points]
    left, right, top, bottom = min(xs), max(xs), min(ys), max(ys)
    if right - left <= TOL or bottom - top <= TOL:
        raise Unassessed("Degenerate node rectangle: " + ident)
    expected = {(left, top), (right, top), (right, bottom), (left, bottom)}
    if {tuple(p) for p in points} != expected:
        raise Unassessed("Non-axis-aligned node rectangle: " + ident)
    for a, b in zip(points, points[1:] + points[:1]):
        if a[0] != b[0] and a[1] != b[1]:
            raise Unassessed("Crossed rectangle path: " + ident)
    return [left, top, right, bottom]


def boundary(point, box):
    x, y = point
    left, top, right, bottom = box
    if not (left - TOL <= x <= right + TOL and top - TOL <= y <= bottom + TOL):
        return False
    return min(abs(x - left), abs(x - right), abs(y - top), abs(y - bottom)) <= TOL


def native_text_stylesheets(root):
    """Accept only this renderer's font declaration and stroke defaults.

    This is an allowlist, not a CSS cascade or font realization check.
    """
    font_face = re.compile(
        r'@font-face\{font-family:"DejaVu Sans";font-style:normal;font-weight:400;'
        r'src:url\(data:font/ttf;base64,[A-Za-z0-9+/=]+\) format\("truetype"\);\}')
    stroke_defaults = '*{stroke-linejoin: round; stroke-linecap: butt}'
    for element in root.iter(NS + "style"):
        if (set(element.attrib) - {"type"} or element.get("type", "text/css") != "text/css"
                or len(element)):
            raise Unassessed("Unsupported native-text stylesheet markup")
        source = (element.text or "").strip()
        if source != stroke_defaults and not font_face.fullmatch(source):
            raise Unassessed("Unsupported native-text stylesheet")


def native_text_presentation(element, parents):
    """Conservative subset; unsupported inherited styling stays unassessed."""
    for item in parents[element]:
        if item.tag == NS + "svg" and item is not parents[element][-1]:
            raise Unassessed("Nested native-text SVG viewport is unsupported")
        allowed = {"id"} if item.tag == NS + "g" else (
            {"width", "height", "viewBox", "version"} if item.tag == NS + "svg" else set())
        if item.tag not in (NS + "g", NS + "svg") or set(item.attrib) - allowed:
            raise Unassessed("Unsupported native-text ancestor presentation")
    pieces = [p.strip() for p in element.get("style", "").split(";") if p.strip()]
    if any(p.count(":") != 1 for p in pieces):
        raise Unassessed("Unsupported native-text glyph style")
    pairs = [tuple(v.strip() for v in p.split(":", 1)) for p in pieces]
    style = dict(pairs)
    if (len(style) != len(pairs) or set(style) != {
            "font-style", "font-weight", "font-size", "font-family", "text-anchor", "fill"}
            or style["font-style"] != "normal" or style["font-weight"] != "400"
            or style["font-family"] != "'DejaVu Sans'" or style["text-anchor"] != "start"
            or not re.fullmatch(r"#[0-9a-fA-F]{6}", style["fill"])):
        raise Unassessed("Unsupported native-text glyph style")
    size = style["font-size"]
    if (not size.endswith("px") or not NUMBER.fullmatch(size[:-2])
            or not math.isfinite(float(size[:-2])) or float(size[:-2]) <= 0):
        raise Unassessed("Unsupported native-text font size")


def text_attachment(raw, index, parents):
    """A reviewed, fixed offset from actual text origins, not a glyph box.

    Complete membership and relative typography are caller-frozen so the
    anchor cannot silently follow an arrow or a detached first glyph.
    """
    if (not isinstance(raw, dict) or set(raw) != {"runs", "glyphs", "offset_pt", "review_note"}
            or not isinstance(raw["review_note"], str) or not raw["review_note"].strip()):
        raise InvalidInput("Text attachment needs runs, glyphs, offset_pt and explicit review_note")
    def pair(value):
        if (not isinstance(value, list) or len(value) != 2
                or any(type(v) not in (int, float) or not math.isfinite(v) for v in value)):
            raise InvalidInput("Text attachment coordinates must be finite pairs")
        return value
    offset = pair(raw["offset_pt"])
    runs, glyphs = raw["runs"], raw["glyphs"]
    if not isinstance(runs, list) or not runs or not isinstance(glyphs, list) or not glyphs:
        raise InvalidInput("Text attachment needs complete nonempty run/glyph lists")
    expected_ids, run_ids, actual_ids = [], [], []
    for glyph in glyphs:
        if (not isinstance(glyph, dict) or set(glyph) != {"group_id", "text", "relative_pt", "style"}
                or not isinstance(glyph["group_id"], str) or not glyph["group_id"]
                or not isinstance(glyph["text"], str) or len(glyph["text"]) != 1
                or not isinstance(glyph["style"], str) or not glyph["style"]):
            raise InvalidInput("Invalid declared native glyph")
        pair(glyph["relative_pt"])
        expected_ids.append(glyph["group_id"])
    if len(set(expected_ids)) != len(expected_ids) or glyphs[0]["relative_pt"] != [0, 0]:
        raise InvalidInput("Text glyph IDs must be unique and first origin relative zero")
    actual_texts = []
    for run in runs:
        if (not isinstance(run, dict) or set(run) != {"group_id", "text"}
                or not isinstance(run["group_id"], str) or not isinstance(run["text"], str)):
            raise InvalidInput("Invalid declared native text run")
        ident = run["group_id"]
        if ident in run_ids:
            raise InvalidInput("Duplicate text run binding")
        run_ids.append(ident)
        group = index.get(ident)
        if group is None or group.tag != NS + "g":
            raise Unassessed("Missing native text run: " + ident)
        visible_chain(group, parents)
        if any(e.tag not in (NS + "g", NS + "text") for e in group.iter()):
            raise Unassessed("Unsupported child in native text run: " + ident)
        texts = [e for e in group.iter() if e.tag == NS + "text"]
        if not texts or "".join(e.text or "" for e in texts) != run["text"]:
            raise Unassessed("Native text run content mismatch: " + ident)
        for element in texts:
            parent = parents[element][0]
            ident = parent.get("id")
            if (ident not in expected_ids or list(parent) != [element] or len(element)
                    or len(element.text or "") != 1):
                raise Unassessed("Native text glyph membership mismatch")
            visible_chain(element, parents, allow_zero_text_rotation=True)
            native_text_presentation(element, parents)
            actual_ids.append(ident)
            actual_texts.append(element)
    if actual_ids != expected_ids:
        raise Unassessed("Native text glyph membership/order mismatch")
    origins = []
    for expected, element in zip(glyphs, actual_texts):
        if element.text != expected["text"] or element.get("style") != expected["style"]:
            raise Unassessed("Native text glyph content/style mismatch")
        if any(k not in {"x", "y", "style", "transform"} for k in element.attrib):
            raise Unassessed("Unsupported native text positioning/presentation attribute")
        values = [element.get(k, "") for k in ("x", "y")]
        if any(not NUMBER.fullmatch(v) for v in values):
            raise Unassessed("Native text needs scalar x/y positions")
        origin = list(map(float, values))
        if not all(math.isfinite(v) for v in origin):
            raise Unassessed("Nonfinite native text position")
        origins.append(origin)
    anchor = origins[0]
    for expected, origin in zip(glyphs, origins):
        relative = [origin[0] - anchor[0], origin[1] - anchor[1]]
        if dist(relative, expected["relative_pt"]) > TOL:
            raise Unassessed("Native text relative glyph positions changed")
    return {"point": [anchor[0] + offset[0], anchor[1] + offset[1]],
            "attachment_kind": "caller_declared_native_text_port",
            "native_origin": anchor, "offset_pt": offset, "run_ids": run_ids,
            "verified_run_strings": [run["text"] for run in runs],
            "glyph_count": len(glyphs), "review_note": raw["review_note"],
            "glyph_ink_contact_checked": False}


def head_ok(points, triangle, closed, ident):
    if closed and len(triangle) == 4 and dist(triangle[0], triangle[-1]) < 1e-9:
        triangle = triangle[:-1]
    if not closed or len(triangle) != 3:
        raise Unassessed("Arrow head is not a native triangle: " + ident)
    end, previous = points[-1], points[-2]
    matches = [i for i, v in enumerate(triangle) if dist(v, end) <= TOL]
    if len(matches) != 1:
        raise Unassessed("Arrow tip does not uniquely match shaft endpoint: " + ident)
    bases = [v for i, v in enumerate(triangle) if i != matches[0]]
    dx, dy = end[0] - previous[0], end[1] - previous[1]
    length = math.hypot(dx, dy)
    if length <= TOL:
        raise Unassessed("Degenerate final arrow segment: " + ident)
    ux, uy = dx / length, dy / length
    dots = [(v[0] - end[0]) * ux + (v[1] - end[1]) * uy for v in bases]
    cross = [(v[0] - end[0]) * uy - (v[1] - end[1]) * ux for v in bases]
    if not all(v < -TOL for v in dots) or cross[0] * cross[1] >= -1e-9:
        raise Unassessed("Reversed or degenerate arrow head: " + ident)


def inventory(svg, bindings):
    data, pin = read(svg)
    if b"<!ENTITY" in data.upper() or re.search(br"<!DOCTYPE[^>]*\[", data, re.I):
        raise InvalidInput("Internal DTD/entities are refused")
    try:
        root = ET.fromstring(data)
    except ET.ParseError as error:
        raise InvalidInput("Invalid SVG XML") from error
    if root.tag != NS + "svg":
        raise InvalidInput("Expected SVG root")
    if root.get("transform"):
        raise Unassessed("Root transform unsupported")
    try:
        view = [float(v) for v in root.get("viewBox", "").split()]
        width = float(root.get("width", "").removesuffix("pt"))
        height = float(root.get("height", "").removesuffix("pt"))
    except ValueError as error:
        raise Unassessed("SVG must use physical point dimensions") from error
    if (not root.get("width", "").endswith("pt") or not root.get("height", "").endswith("pt")
            or len(view) != 4 or view[:2] != [0, 0] or view[2:] != [width, height]
            or not all(math.isfinite(v) for v in view) or width <= 0 or height <= 0):
        raise Unassessed("SVG units/viewBox are unsupported")
    index, parents = {}, {}
    def visit(element, ancestors):
        parents[element] = tuple(ancestors)
        ident = element.get("id")
        if ident:
            if ident in index:
                raise InvalidInput("Duplicate SVG ID: " + ident)
            index[ident] = element
        if element.tag in (NS + "image", NS + "marker"):
            raise Unassessed("Raster/marker arrows are outside this vector convention")
        if any(element.get(k) for k in ("marker-start", "marker-mid", "marker-end")):
            raise Unassessed("SVG marker arrows are unsupported")
        for child in element:
            visit(child, [element, *ancestors])
    visit(root, [])
    if bindings.get("schema") != "mcf-svg-node-bindings-v1" or bindings.get("convention") != "mcf-separated-shaft-head-v1":
        raise InvalidInput("Unsupported node-binding schema/convention")
    shafts = {ident[:-7] for ident in index if ident.endswith("--shaft")}
    heads = {ident[:-6] for ident in index if ident.endswith("--head")}
    plain = bindings.get("non_arrow_shafts", {})
    if (not isinstance(plain, dict) or not set(plain) <= shafts - heads
            or any(not isinstance(reason, str) or not reason.strip() for reason in plain.values())):
        raise InvalidInput("Plain shafts need existing unheaded IDs and explicit reasons")
    if not heads or shafts - set(plain) != heads:
        raise Unassessed("Named shaft/head sets are empty or do not match")
    excluded = bindings.get("excluded_arrows", {})
    if (not isinstance(excluded, dict) or not set(excluded) <= shafts
            or any(not isinstance(reason, str) or not reason.strip() for reason in excluded.values())):
        raise InvalidInput("Excluded arrows need existing IDs and explicit reasons")
    arrows = {}
    for ident in sorted(heads):
        points, closed = single_path(ident + "--shaft", index, parents)
        if closed or len(points) < 2 or any(dist(a, b) <= 1e-9 for a, b in zip(points, points[1:])):
            raise Unassessed("Invalid open polyline shaft: " + ident)
        triangle, closed_head = single_path(ident + "--head", index, parents)
        head_ok(points, triangle, closed_head, ident)
        arrows[ident] = points
    raw_nodes = bindings.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise InvalidInput("Node bindings must be a nonempty list")
    if any(isinstance(raw, dict) and "text_attachment" in raw for raw in raw_nodes):
        # ElementTree drops processing instructions. Refuse non-declaration
        # PIs before that omission can hide a stylesheet from the allowlist.
        if re.search(br"<\?(?!xml\s)", data, re.I):
            raise Unassessed("Native-text XML processing instructions are unsupported")
        native_text_stylesheets(root)
    nodes = {}
    for raw in raw_nodes:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str) or not raw["id"]:
            raise InvalidInput("Invalid node ID")
        ident = raw["id"]
        if ident in nodes:
            raise InvalidInput("Duplicate bound node ID: " + ident)
        if sum(k in raw for k in ("shape_id", "point_from_arrow", "text_attachment")) != 1:
            raise InvalidInput("Node needs exactly one rectangle, junction or text attachment binding")
        if "shape_id" in raw and "point_from_arrow" not in raw:
            nodes[ident] = {"shape_id": raw["shape_id"],
                            "box": rectangle(raw["shape_id"], index, parents)}
        elif "point_from_arrow" in raw and "shape_id" not in raw:
            arrow, vertex = raw["point_from_arrow"], raw.get("vertex_index")
            if arrow not in arrows or arrow in excluded or type(vertex) is not int or not 0 <= vertex < len(arrows[arrow]):
                raise InvalidInput("Invalid junction binding: " + ident)
            contacts = raw.get("connected_to_arrows")
            if (not isinstance(contacts, list) or not contacts
                    or any(not isinstance(v, str) for v in contacts)
                    or len(set(contacts)) != len(contacts)
                    or any(v not in arrows or v == arrow or v in excluded for v in contacts)):
                raise InvalidInput("Junction needs explicit other carrier arrows: " + ident)
            point = arrows[arrow][vertex]
            if any(distance_to_polyline(point, arrows[v]) > TOL for v in contacts):
                raise Unassessed("Junction contact with declared carrier missing: " + ident)
            nodes[ident] = {"point_from_arrow": arrow, "vertex_index": vertex,
                            "point": point, "connected_to_arrows": contacts}
        elif "text_attachment" in raw:
            nodes[ident] = text_attachment(raw["text_attachment"], index, parents)
    def candidates(point):
        return [ident for ident, node in nodes.items()
                if (boundary(point, node["box"]) if "box" in node
                    else dist(point, node["point"]) <= TOL)]
    records, unresolved = [], []
    for ident, points in arrows.items():
        if ident in excluded:
            continue
        source, target = candidates(points[0]), candidates(points[-1])
        record = {"arrow_id": ident, "source_point": points[0], "target_point": points[-1],
                  "path_points": points, "source_candidates": source, "target_candidates": target}
        if len(source) == len(target) == 1:
            record.update(source=source[0], target=target[0])
        else:
            unresolved.append({"arrow_id": ident, "source_candidates": source,
                               "target_candidates": target, "reason": "Unbound or ambiguous endpoint"})
        records.append(record)
    text_nodes = [k for k, v in nodes.items() if v.get("attachment_kind") == "caller_declared_native_text_port"]
    return {"svg": pin, "nodes": nodes, "arrows": records, "excluded_arrows": excluded,
            "declared_text_attachment_nodes": text_nodes,
            "text_attachment_scope": "Caller-declared offsets from actual native text origins; no glyph-ink contact proof" if text_nodes else None,
            "non_arrow_shafts": plain,
            "named_arrows_total": len(arrows), "unresolved": unresolved,
            "complete_within_declared_bindings": not unresolved}


def evaluate(before, plan, after=None):
    if plan.get("schema") != "mcf-svg-repair-plan-v1":
        raise InvalidInput("Unsupported repair-plan schema")
    for key in ("remove", "restore", "preserve", "required_edges"):
        if not isinstance(plan.get(key), list):
            raise InvalidInput("Plan needs list: " + key)
    if before["unresolved"] or (after is not None and after["unresolved"]):
        return {"status": "unassessed", "errors": [], "actions": [],
                "reason": "Incomplete endpoint inventory; absence and complete repair cannot be certified"}
    current = {v["arrow_id"]: (v["source"], v["target"]) for v in before["arrows"]}
    node_ids, errors, actions = set(before["nodes"]), [], []
    seen_actions = set()
    def pair(raw, needs_id=True):
        if not isinstance(raw, dict) or any(not isinstance(raw.get(k), str) or not raw[k]
                                           for k in ("source", "target")):
            raise InvalidInput("Action/required edge needs source and target IDs")
        if raw["source"] not in node_ids or raw["target"] not in node_ids:
            raise InvalidInput("Unknown node in plan")
        if needs_id and (not isinstance(raw.get("arrow_id"), str) or not raw["arrow_id"]):
            raise InvalidInput("Action needs arrow_id")
        return raw["source"], raw["target"]
    removed, restored = set(), {}
    for kind in ("remove", "preserve"):
        for raw in plan[kind]:
            expected = pair(raw)
            ident = raw["arrow_id"]
            if (kind, ident) in seen_actions:
                raise InvalidInput("Duplicate operation: " + kind + "/" + ident)
            seen_actions.add((kind, ident))
            actual = current.get(ident)
            valid = actual == expected
            code = None if valid else ("arrow_absent" if actual is None else "current_endpoint_mismatch")
            actions.append({"operation": kind, **raw, "actual": list(actual) if actual else None,
                            "valid": valid, "error": code})
            if not valid:
                errors.append({"code": code, "operation": kind, "arrow_id": ident})
            if kind == "remove" and valid:
                removed.add(ident)
    overlap = {x["arrow_id"] for x in plan["preserve"]} & {x["arrow_id"] for x in plan["remove"]}
    if overlap:
        errors.append({"code": "remove_preserve_conflict", "arrow_ids": sorted(overlap)})
    for raw in plan["restore"]:
        expected = pair(raw)
        ident = raw["arrow_id"]
        if ("restore", ident) in seen_actions:
            raise InvalidInput("Duplicate restoration ID")
        seen_actions.add(("restore", ident))
        code = ("edge_already_present" if expected in current.values()
                else "restoration_id_in_use" if ident in restored or (ident in current and ident not in removed)
                else None)
        actions.append({"operation": "restore", **raw, "valid": code is None, "error": code})
        if code:
            errors.append({"code": code, "operation": "restore", "arrow_id": ident})
        else:
            restored[ident] = expected
    post = {ident: edge for ident, edge in current.items() if ident not in removed}
    post.update(restored)
    required = [pair(raw, False) for raw in plan["required_edges"]]
    if len(set(required)) != len(required):
        raise InvalidInput("Duplicate required edge")
    missing = [list(edge) for edge in required if edge not in post.values()]
    if missing:
        errors.append({"code": "required_edge_missing", "edges": missing})
    for raw in plan["preserve"]:
        if post.get(raw["arrow_id"]) != pair(raw):
            errors.append({"code": "preserved_edge_not_in_postgraph", "arrow_id": raw["arrow_id"]})
    after_matches = None
    if after is not None:
        actual_after = {v["arrow_id"]: (v["source"], v["target"]) for v in after["arrows"]}
        after_matches = actual_after == post and set(after["nodes"]) == node_ids
        if not after_matches:
            errors.append({"code": "after_graph_mismatch",
                           "expected": {k: list(v) for k, v in post.items()},
                           "actual": {k: list(v) for k, v in actual_after.items()}})
    return {"status": "fail" if errors else "pass", "errors": errors, "actions": actions,
            "missing_required_edges": missing,
            "proposed_postgraph": {k: list(v) for k, v in post.items()},
            "actual_after_graph_matches": after_matches}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--svg", type=Path, required=True)
    parser.add_argument("--bindings", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--after-svg", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    scope = ("Named SVG geometry and proposed operations only; native-text ports, if supplied, use "
             "caller-declared offsets rather than glyph-ink contact. Source-approved required edges and "
             "bindings are supplied by the caller. No label/scientific validity, full CSS visibility, "
             "general SVG/editor compatibility or medical accuracy claim. Actual viewing remains required.")
    pins = []
    result = {"schema": "mcf-svg-repair-check-v1", "scope": scope,
              "scientific_validity_checked": False, "tolerance_pt": TOL}
    writable = False
    try:
        out = guard(args.out)
        if out.exists():
            raise InvalidInput("Existing output refused: " + str(out))
        if not out.parent.is_dir():
            raise InvalidInput("Output parent must already exist")
        writable = True
        for path in [args.bindings, args.plan, args.svg] + ([args.after_svg] if args.after_svg else []):
            _, input_pin = read(path)
            pins.append(input_pin)
        bindings, binding_pin = read_json(args.bindings)
        plan, plan_pin = read_json(args.plan)
        before = inventory(args.svg, bindings)
        after = inventory(args.after_svg, bindings) if args.after_svg else None
        result.update(before=before, after=after, evaluation=evaluate(before, plan, after))
        result["status"] = result["evaluation"]["status"]
        for pin in pins:
            _, observed = read(pin["path"])
            if observed != pin:
                raise InvalidInput("Input changed during check")
    except Unassessed as error:
        result.update(status="unassessed", error=str(error))
    except (InvalidInput, OSError, TypeError, KeyError) as error:
        result.update(status="fail", error=str(error))
    result["input_pins"] = pins
    result["actual_after_svg_checked"] = args.after_svg is not None and result.get("after") is not None
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if writable:
        try:
            with args.out.open("x", encoding="utf-8") as output:
                output.write(text)
        except OSError as error:
            print("Output refused: " + str(error), file=sys.stderr)
            return 1
    print(json.dumps({"status": result["status"], "output": str(args.out) if writable else None,
                      "error": result.get("error"), "scope": scope}, ensure_ascii=False))
    return 0 if result["status"] == "pass" else 2 if result["status"] == "unassessed" else 1


if __name__ == "__main__":
    sys.exit(main())

