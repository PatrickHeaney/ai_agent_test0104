This document outlines the specific implementation tasks for building the AI Agent, organized by iteration as defined in `PLANNING.md`.

## Iteration 1: The Core Conversation Loop

### Project Setup
- [x] Read, or is missing create, `requirements.txt` file with pinned major versions (e.g., `pydantic-ai~=1.0`, `pytest-asyncio~=0.23`). Only modify it if there are new dependencies or new versions are required.
- [x] Read, or is missing create, `.env.example` file with `LLM_BASE_URL`, `LLM_API_KEY`, and `LLM_CHOICE`.
- [x] Create the initial file structure (`agent.py`, `cli.py`, `tests/`).
- [x] Create a `pytest.ini` file in the root to configure `testpaths` and `pythonpath`.

### Agent Core (`agent.py`)
- [x] Implement an `AIAgent` class.
- [x] The constructor `__init__` should initialize the agent using `pydantic-ai`'s `Agent` class, loading configuration from environment variables.
      - **Hint:** Use `from pydantic_ai.models.openai import OpenAIChatModel` and `from pydantic_ai.providers.openai import OpenAIProvider`.
      - **Hint:** The `Agent` class constructor uses the `model=` keyword argument (e.g., `Agent(model=...)`).
- [x] Implement an `async def chat` method that calls the agent's `.run()` method and returns the `.output` of the result.

### Terminal UI (`cli.py`)
- [x] Create the main application entry point as an `async def main` function.
- [x] Use `import asyncio` and `asyncio.run(main())` to start the application.
- [x] Implement a `while` loop to continuously accept user input.
- [x] Call the agent's `chat` method (using `await`) and print the response.
- [x] Add a way for the user to exit the application (e.g., typing 'exit').

### Testing (`tests/`)
- [x] Write a unit test in `tests/test_agent.py` to verify the `AIAgent` class can be initialized.
- [x] Write an async unit test using `pytest-asyncio` to check the conversation loop. This test should mock the `agent.run` method.

### Documentation
- [x] Update `README.md` with setup and usage instructions using `uv` for all commands.

---

## Iteration 2: Adding Memory (Future)
- [ ] ...

## Iteration 3: Adding Web Search (Future)
- [ ] ...
