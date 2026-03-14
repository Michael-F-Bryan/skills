# Container Health Agent

Purpose

Evaluate structural quality of PARA containers.

## Inputs

```
survey-report.json
activity-report.json
classification-report.json
```

## Tasks

Detect:

Containers too broad.

Duplicate topics.

Containers that should be archived.

Containers that may need splitting.

## Output

```
container-health-report.json
```

Example

```
{
  "broad_containers": [],
  "duplicate_topics": [],
  "archive_candidates": [],
  "split_candidates": []
}
```

## Evaluation criteria

Prefer stability.

Avoid proposing structural change unless evidence is strong.

When uncertain:

- mark `"confidence": "low"`
