
# Contributing Tests

## Guidelines

- Keep each test focused on one behavior.
- Use descriptive test names.
- Use small, predictable sample data.
- Keep tests separate from application source code.
- Check the existing implementation before writing assertions.
- Run tests from the project root before submitting a pull request.
- Investigate test failures before proposing changes for merging.

## AQI Feature Tests

Tests may cover season classification, next-day AQI targets, and rolling statistics.

Assertions should match the actual project implementation and expected behavior.

## Reporting Failures

When a test fails, record the error and investigate its cause. Do not claim that a test passes until it has run successfully.
