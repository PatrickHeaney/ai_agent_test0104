# Upgrade Plan for ai_agent_test0104

This document summarizes the lessons learned from previous projects and outlines the necessary upgrades to the `_new_prj` template. The goal is to create a robust, clear, and consistent starting point for the next agent implementation.

## 1. Harden Project Dependencies and Configuration

*   **Action:** Update `requirements.txt` to pin major versions of key libraries.
*   **Reason:** Prevents breaking changes from library updates, as seen with `pydantic-ai`.
*   **Content:**
    ```
    pydantic-ai~=1.0
    openai~=1.0
    python-dotenv~=1.0
    pytest~=8.0
    pytest-asyncio~=0.23
    ```

*   **Action:** Create a `pytest.ini` file in the project root.
*   **Reason:** Simplifies the test command to `uv run pytest` and prevents `pytest` from discovering tests in submodules or failing to find local modules.
*   **Content:**
    ```ini
    [pytest]
    testpaths = tests
    pythonpath = .
    ```

## 2. Update Core Instructions for Modern `pydantic-ai`

*   **Action:** Modify `TASK.md` to be highly specific about the implementation details for Iteration 1.
*   **Reason:** The `pydantic-ai` API has changed significantly. The instructions must guide the agent to use the correct, modern, asynchronous patterns.
*   **Specific Changes to `TASK.md`:**
    *   **Agent Core:** Mandate an `async def chat` method. Specify the exact classes to use: `Agent`, `OpenAIChatModel`, and `OpenAIProvider`.
    *   **Terminal UI:** Mandate an `async def main` function and the `asyncio.run(main())` entry point.
    *   **Testing:** Add a task to create the `pytest.ini` file. Mandate `pytest-asyncio` for testing async functions.

## 3. Ensure Documentation Consistency

*   **Action:** Update `PLANNING.md` and `README.md` to reflect the new project structure and processes.
*   **Reason:** Documentation must be accurate and consistent to avoid confusion.
*   **Specific Changes:**
    *   In `PLANNING.md` and `README.md`, add `pytest.ini` to the file structure diagrams.
    *   In `README.md`, update all setup, installation, and execution commands to use the `uv` toolchain (e.g., `uv venv`, `uv pip install`, `uv run cli.py`, `uv run pytest`).
    *   In `README.md`, add a "Running Tests" section that explains the simple `uv run pytest` command.

*   **Action:** Correct the iteration order in `PLANNING.md` and `README.md`.
*   **Reason:** The desired iteration order is Memory then Web Search.
*   **Specific Changes:** Ensure future iterations are listed as 1) Core Loop, 2) Memory, 3) Web Search.

## 4. Update `start_clone_create.md`

*   **Action:** No major changes are needed, but review to ensure clarity, especially around the submodule initialization step. The current phrasing, "Download Example Code Submodules," is clear and should be kept.
