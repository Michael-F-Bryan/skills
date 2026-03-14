# Repo Survey Agent

Purpose

Identify recent repository activity and anomalies.

## Inputs

Repository root.

Git history.

Filesystem tree.

## Tasks

Collect:

- files modified within recent window
- newly created files
- files outside PARA roots
- containers recently touched

PARA roots:

```
1-projects
2-areas
3-resources
4-archives
```

## Output

```
survey-report.json
```

Example

```
{
  "recent_files": [],
  "new_files": [],
  "outside_para": [],
  "active_containers": []
}
```

## Evaluation criteria

A good report:

- accurately lists recent files
- highlights anomalies
- contains no speculative interpretation

The agent must not classify or reorganise files at this stage.

It only gathers signals.
