# Calibration note: Greenfield size discipline

Dimension reminder: tendency to keep greenfield work compact and domain-shaped versus architecture theatre that inflates file count and LOC without proportional complexity. These counts describe hypothetical examples, not limits or target shapes for new work.

See also: dimension-07 (abstraction threshold), dimension-15 (entry points), dimension-16 (repo topology).

---

```python
# Small CSV→JSON CLI — ACCEPTABLE greenfield shape
# csvjson/cli.py, transform.py, types.py, io.py — ~120 LOC production
# Tests exercise real files and CliRunner; no service/repository layers
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - Thin CLI, typed row models at boundary, pure transform, IO at edge
  - Each file owns a distinct responsibility in this hypothetical tool; another coherent layout could also work
  - No Manager/Service/Repository vocabulary

---

```python
# Same CSV→JSON task — REJECTED slop shape
# src/
#   interfaces/csv_reader.py
#   interfaces/json_writer.py
#   services/conversion_service.py
#   repositories/row_repository.py
#   models/dto.py, models/entity.py
#   factories/pipeline_factory.py
#   validators/row_validator.py
#   cli/main.py
# ~600+ LOC production
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - Architecture nouns outnumber domain nouns; every layer is a pass-through for a task that fits in one pipeline function
  - Here the interfaces merely forward calls; a single-implementation interface can be useful at a real external boundary

---

```python
# ~80 LOC utils refactor — ACCEPTABLE split
# user_utils/validation.py  (email rules)
# user_utils/users.py       (build_user_record, process_users_file)
# user_utils/io.py          (json load/save if reused)
```

- Score (1-5): 4
- Confidence (`low|medium|high`): medium
- Evidence:
  - The split follows distinct responsibilities rather than pattern vocabulary
  - The IO module is conditional on actual reuse, not required by the example's size

---

```python
# Same ~80 LOC refactor — REJECTED over-split
# validation.py, dates.py, text.py, io.py, users.py, __init__.py
# Five modules for trivial helpers used once
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - In this example `dates.py` and `text.py` merely relocate trivial call-site code; their names don't identify coherent responsibilities
  - A single-use helper can still earn its place if it encapsulates real complexity or makes the caller clearer
