# Activity Detection Agent

Purpose

Detect patterns of current work and knowledge formation.

## Inputs

```
survey-report.json
```

## Tasks

Identify:

Active projects

Signals:

- multiple edits
- plans or reports
- execution artefacts

Dormant projects

Signals:

- no changes for extended period

Emerging topics

Signals:

- several new files about same concept
- repeated terms across changed files

Distillation candidates

Signals:

- repeated principles
- recurring reasoning patterns

## Output

```
activity-report.json
```

Example

```
{
  "active_projects": [],
  "dormant_projects": [],
  "emerging_topics": [],
  "distillation_candidates": []
}
```

## Evaluation criteria

Good outputs:

- grounded in repo evidence
- avoid speculation
- highlight clusters of activity

If uncertain:

- mark with `"confidence": "low"`
