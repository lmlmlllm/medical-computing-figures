#!/usr/bin/env python3
"""Read-only check of the designated current STATUS summary against catalog JSONL.

This bounded prose format is used before the first level-two Markdown heading.
Historical paragraphs are ignored. Paper identities are stored strings, not
normalized bibliographic entities; legacy rows are not newly certified.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True


class InputError(ValueError):
    pass


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise InputError(f"Duplicate JSON member: {key}")
        result[key] = value
    return result


def reject_constant(value):
    raise InputError(f"Non-JSON constant: {value}")


def read_input(value):
    path = Path(value).absolute()
    for part in (path, *path.parents):
        if part.is_symlink():
            raise InputError(f"Symlink input/ancestor rejected: {part}")
    data = path.read_bytes()
    return data.decode("utf-8"), {
        "path": str(path), "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def expected_counts(text):
    rows, ids = [], set()
    counts = {"semantic_partial": 0, "full_joint_verified": 0, "legacy": 0}
    for line_number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line, object_pairs_hook=unique_object,
                             parse_constant=reject_constant)
        except json.JSONDecodeError as exc:
            raise InputError(f"Catalog line {line_number}: {exc.msg}") from exc
        except InputError as exc:
            raise InputError(f"Catalog line {line_number}: {exc}") from exc
        if not isinstance(row, dict):
            raise InputError(f"Catalog line {line_number}: expected object")
        for field in ("id", "paper"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise InputError(f"Catalog line {line_number}: nonempty {field} string required")
        if row["id"] in ids:
            raise InputError(f"Duplicate catalog id at line {line_number}: {row['id']}")
        ids.add(row["id"])
        if "semantic_status" not in row:
            counts["legacy"] += 1
        elif row["semantic_status"] in ("semantic_partial", "full_joint_verified"):
            counts[row["semantic_status"]] += 1
        else:
            raise InputError(f"Unsupported semantic_status at line {line_number}: {row['semantic_status']!r}")
        rows.append(row)
    if not rows:
        raise InputError("Catalog is empty")
    return {
        "entries": len(rows), "papers": len({row["paper"] for row in rows}),
        "partial": counts["semantic_partial"], "full": counts["full_joint_verified"],
        "legacy": counts["legacy"],
        "historical": counts["legacy"] + counts["full_joint_verified"],
        "latest": rows[-1]["id"],
    }


SUMMARY = re.compile(
    r"^目录现为(?P<entries>\d+)条[／/](?P<papers>\d+)篇，"
    r"(?P<partial>\d+)个partial条目与(?P<historical>\d+)个历史完整条目；"
    r"后者含(?P<legacy>\d+)个较早未重审条目和(?P<full>\d+)个显式完整核验条目。"
    r"最新入库为(?P<latest>[A-Za-z0-9_-]+)，"
)


def observed_counts(text):
    preface = re.split(r"^##\s+", text, maxsplit=1, flags=re.MULTILINE)[0]
    matches = [(n, line.strip()) for n, line in enumerate(preface.splitlines(), 1)
               if line.strip().startswith("目录现为")]
    if len(matches) != 1:
        raise InputError(f"Expected exactly one current summary before first ## heading; found {len(matches)}")
    line_number, line = matches[0]
    match = SUMMARY.match(line)
    if not match:
        raise InputError(f"Current summary line {line_number} does not match the supported explicit count format")
    values = match.groupdict()
    return {key: value if key == "latest" else int(value)
            for key, value in values.items()}, line_number


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", required=True, help="STATUS.md input")
    parser.add_argument("--catalog", required=True, help="catalog.jsonl input")
    args = parser.parse_args()
    try:
        status, status_pin = read_input(args.status)
        catalog, catalog_pin = read_input(args.catalog)
        expected = expected_counts(catalog)
        observed, line = observed_counts(status)
        mismatches = [{"field": key, "observed": observed[key], "expected": expected[key]}
                      for key in expected if expected[key] != observed[key]]
        result = {"status": "mismatch" if mismatches else "consistent",
                  "summary_line": line, "observed": observed, "expected": expected,
                  "mismatches": mismatches, "inputs": [status_pin, catalog_pin],
                  "scope": "Current preface summary only; stored paper identities; legacy is not newly certified."}
        code = 1 if mismatches else 0
    except (InputError, OSError, UnicodeError) as exc:
        result, code = {"status": "invalid_input", "error": str(exc)}, 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
