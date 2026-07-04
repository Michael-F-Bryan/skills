# Refactor utils dumping ground

## Unprompted arm

This directory contains a small Python module `fixture/utils.py` with unrelated helpers dumped together, a subtle email validation bug (`validate_email` accepts `"foo@"`), and weak tests.

Refactor it into cohesive modules with clear domain boundaries. Fix the email validation bug. Add tests that prove the bug is fixed and that `process_users_file` works end-to-end.

Constraints:
- Stay surgical — this is a small module, not a greenfield rewrite
- Keep the public workflow (`process_users_file`) working
- Put your refactored code in `output/` as a proper small package

## Explicit arm

Same task, but you **must** read and apply the `code-like-michael` skill first.

## Grading notes

- Did agent avoid drive-by rearchitecture (service/repository layers)?
- Cohesive module split vs utils dump?
- Surgical change scope?
- Tests prove behaviour not mocks?
