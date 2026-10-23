# Selective read-only migration — 2026-10-11

Read versions and SHA256 are in `tests/legacy_read_manifest.json`. Old root was `<LOCAL_HOME>/.codex/skills/biomedical-figure-style`; this is provenance only. No old files/scripts were written or executed. No old image was copied. The old directory may be concurrently maintained; a later hash difference alone is not attributed to this task.

| Read source / scope | Decision and reason | New implementation | Verification |
|---|---|---|---|
| SKILL.md; figure_logic_CN.md | Adjust: bidirectional source/image checks, separate semantic/visual properties; add algorithm stage/interface/data-level constraints | SKILL, understanding, drawing-and-review, specification | Controlled test evidence recorded under tests; old PASS not inherited |
| continuous_search_objective_CN.md | Adjust: ≤10 figures, dedup, conditional rules and checkpoint useful; journal-review-only/rolling-three-year/disease rotation not applicable | learning.md, catalog | Batch/case manifests retain access limitations |
| style_tokens.json, P01 and common only | Adjust: neutral low-saturation defaults; old palette is a design recommendation, not newly confirmed preference | assets/style.json | Actual generated figures inspected; preserve source palette status |
| validate_figure_logic.py, full read | Adjust algorithm: stable-ID validation and semantic/visual split; do not copy code because no explicit reuse license was found | Independently written check_spec.py and render.py | Deterministic tests + independent visual checks, not medical proof |
| catalog.json B01-01 metadata only | Do not adopt its biological scene. Retain useful version/status boundaries; archived does not mean scientifically verified | independent MCF IDs and status axes | No old scientific verification imported |
| design_cards.json keys and first-card query | No cards returned at this read; no claim that previous semantic cases were completed | New cases built from primary sources | Old capability remains unverified in this task |

Source code, configuration recommendations and third-party images are treated separately. The new code was written for this task; no third-party original artwork enters the distributable skill unless explicitly allowed and attributed. Runtime independence is verified separately from this historical source record.
