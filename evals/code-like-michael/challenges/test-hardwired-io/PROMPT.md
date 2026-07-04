# Test hard-wired IO component

## Unprompted arm

The `fixture/weather.py` module fetches weather over HTTP with hard-wired `urllib` and `datetime.now()`. Write a proper test suite for `classify_comfort` and `fetch_weather` without mock theatre.

Put tests in `output/tests/` and refactor the production code in `output/weather/` only as much as needed for testability.

Constraints:
- Do not patch `urllib.request.urlopen` or `datetime.now` on the module under test
- Tests must be deterministic and hermetic
- Assert observable outcomes

## Explicit arm

Same task, but you **must** read and apply the `code-like-michael` skill first.

## Grading notes

- Injection vs monkeypatching?
- Real `classify_comfort` tests?
- Fake HTTP seam vs patching urlopen?
