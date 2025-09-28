# Lesson Learned: Deviations from TASK.md During Iteration 1

## 1. Problem Summary

During the implementation of the agent's first iteration, two deviations from the `TASK.md` checklist occurred. This document outlines what happened and provides recommendations for updating the source template to prevent confusion in the future.

## 2. Deviations and Recommendations

### Deviation 1: `.env.example` File Was Not Created
✅ Resolved - the .env.example file already exists in the repository.  I update the step to confirm or modify the file as needed.
- **What Happened:** The task `[ ] Create .env.example with LLM_BASE_URL, LLM_API_KEY, and LLM_CHOICE` was not completed. The operation was explicitly skipped by the user.
- **Impact:** The final project state is missing the `.env.example` file. This means a new developer cannot see which environment variables are required for the application to run without reading the source code.
- **Recommendation for Template:** The `.env.example` file is critical for usability. The template repository should **ensure** this file is present and committed. The task should be considered a mandatory setup step, not an optional one.

### Deviation 2: Testing Framework Mismatch
[] Fixed in _new_prj
- **What Happened:** The task `[ ] Configure pytest` was interpreted as creating tests that are compatible with `pytest`. The actual tests in `tests/test_agent.py` were written using Python's standard `unittest` library, not with `pytest`-specific syntax (e.g., fixtures, plain `assert` statements).
- **Impact:** While `pytest` can discover and run `unittest` test cases, the test code does not follow the idiomatic `pytest` style. This can be confusing for developers expecting to see and write `pytest`-style tests.
- **Recommendation for Template:** To ensure consistency, the template should be updated in one of two ways:
    1.  **(Preferred)** The example test file (`tests/test_agent.py`) should be refactored to use idiomatic `pytest` syntax. This provides a better and more consistent example for future development.
    2.  **(Alternative)** The task in `TASK.md` should be changed from `[ ] Configure pytest` to something more generic like `[ ] Write unit tests for the agent`, removing the specific framework mention if `unittest` is considered acceptable.
