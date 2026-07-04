# Calibration note: Greenfield size discipline

Dimension reminder: tendency to keep greenfield work compact and domain-shaped versus architecture theatre that inflates file count and LOC without proportional complexity.

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
  - Four files each with one reason to change
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
  - Interfaces with one implementation; classic path to unnecessary LOC growth

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
  - Two or three modules max at this size
  - Split follows domain concerns, not pattern vocabulary

---

```python
# Same ~80 LOC refactor — REJECTED over-split
# validation.py, dates.py, text.py, io.py, users.py, __init__.py
# Five modules for trivial helpers used once
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - `dates.py` and `text.py` are single-function files with no reuse pressure
  - Extraction policy should wait for complexity; inline or merge until then
