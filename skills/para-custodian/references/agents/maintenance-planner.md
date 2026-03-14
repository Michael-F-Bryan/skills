# Maintenance Planner Agent

Purpose

Combine all reports into a final maintenance plan.

## Inputs

```
survey-report.json
activity-report.json
classification-report.json
container-health-report.json
atomic-notes-report.json
```

## Tasks

Determine:

Safe changes.

Structural proposals.

Atomic notes to create.

Archive candidates.

## Output

```
maintenance-plan.md
```

Structure

```
# PARA Maintenance Report

## Activity Summary

## Classification Issues

## Container Health

## Atomic Notes

## Safe Changes

## Structural Proposals

## Next Actions
```

## Evaluation criteria

The final plan must:

- clearly separate safe vs structural changes
- reference earlier reports
- remain concise

Large structural changes must follow the proposal protocol:

```
references/proposals.md
```
