
# AQI Awareness Assistant — Tests

## Purpose
This folder contains tests and checks for the AQI Awareness Assistant project.

## Running the tests
From the project root, install the required project dependencies and run:

```bash
python -m pytest tests/
```

## Feature Structure Check
The `test_build_features.py` file checks whether the feature-engineering source file exists and defines the `get_season_name` function.

This is a structural check. It does not validate AQI predictions or all feature calculations.

## Contribution Guidelines
- Keep tests separate from application code.
- Write small, readable tests.
- Run tests before submitting a pull request.
- Investigate test failures before proposing changes for merging.
