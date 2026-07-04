# Grading rubric

Score each dimension with evidence. Use anchors from `skills/code-like-michael/references/annotations-rubric.md`.

## Activation (binary + notes)

| Result | Criteria |
|--------|----------|
| **Activated** | Agent read `code-like-michael` before writing code (check run summary or tool log) |
| **Not activated** | Agent wrote code without reading skill |

Note: Sub-agents without `available_skills` context will false-negative. Include skill in context for fair activation tests.

## Adherence dimensions

### 1. Size discipline (greenfield)

| Score | Evidence |
|-------|----------|
| Pass | Within tripwire budget OR over with justified reason in self-check |
| Warn | 10-20% over budget, no theatre layers |
| Fail | Slop territory (8+ files / 500+ LOC on small task) with service/repository layers |

### 2. Abstraction pressure

| Score | Evidence |
|-------|----------|
| Pass | Every module/layer passes gate; types at boundaries justified |
| Fail | Manager/Service/Repository pass-through, interfaces with one impl |

### 3. Testing quality

| Score | Evidence |
|-------|----------|
| Pass | Observable outcomes, injection at boundaries, no patch-under-test |
| Fail | Mock choreography, monkeypatched module globals |

### 4. Surgical discipline (refactor)

| Score | Evidence |
|-------|----------|
| Pass | Minimal delta, cohesive split, bug fixed with behaviour tests |
| Fail | Drive-by rearchitecture, over-split tiny modules |

### 5. Reshape pass

| Score | Evidence |
|-------|----------|
| Pass | Agent deleted excess structure, ran self-audit checklist |
| Fail | First-draft architecture presented as final |

## Slop metrics (quick)

Record for every run:

```
skill_activated: yes/no
production_files: N
production_loc: N
architecture_layers: [list]
tests_run: pass/fail
self_check_included: yes/no
```

## Comparison arms

- **Unprompted**: plain task, skill in available_skills only
- **Explicit**: prompt requires applying code-like-michael

If explicit >> unprompted, fix activation (frontmatter, opening block). If both fail adherence, fix tripwires and examples.
