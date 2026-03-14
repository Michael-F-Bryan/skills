# Classification Review Agent

Purpose

Ensure files are located in correct PARA containers.

## Inputs

```
survey-report.json
activity-report.json
```

## Tasks

Evaluate each file:

Does it belong in:

```
1-projects
2-areas
3-resources
4-archives
```

Rules

Projects

Active outcome with finish line.

Areas

Ongoing responsibilities.

Resources

Reference knowledge.

Archives

Inactive material.

## Output

```
classification-report.json
```

Example

```
{
  "misclassified_files": [],
  "recommended_moves": []
}
```

## Evaluation criteria

Moves must:

- improve clarity
- respect shallow PARA structure
- avoid introducing nesting

When uncertain:

- annotate reasoning
- avoid aggressive reclassification
