# AI Agent Baseline

This project is a baseline starting point for creating new AI agents. It begins with the simplest possible runnable agent and will be built upon in future iterations.

## Iteration 1: The Core Conversation Loop

The current version focuses on the core conversation loop.

*   **Goal**: Create the simplest possible, runnable agent.
*   **Functionality**: A user can start the terminal UI, have a basic conversation with the agent (no tools, no memory), and the agent will respond using the LLM.

## Future Iterations

- **Iteration 2:** Adding conversational memory.
- **Iteration 3:** Adding a web search tool.

## Project Structure

```
.
├── .env.example
├── pytest.ini
├── requirements.txt
├── README.md
├── PLANNING.md
├── agent.py           # Main agent implementation
├── cli.py             # Terminal user interface
└── tests/
    └── test_agent.py
```

## Setup Instructions

### Prerequisites

- Python 3.11+

### Environment Setup

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Create a virtual environment and install dependencies:
    ```bash
    uv venv && uv pip install -r requirements.txt
    ```
4.  Create a `.env` file from the example:
    ```bash
    cp .env.example .env
    ```
5.  Configure your `.env` file with your LLM provider details:

    ```
    # Base URL for the OpenAI compatible instance
    # e.g., https://api.openai.com/v1 or http://localhost:11434/v1 for Ollama
    LLM_BASE_URL=

    # API key for your LLM provider
    LLM_API_KEY=

    # The LLM you want to use for the agent
    # e.g., gpt-4o-mini or ollama/qwen2
    LLM_CHOICE=
    ```

## Running the Agent

To start the agent, use `uv run`:

```bash
uv run cli.py
```

You can now chat with the agent. Type `exit` to end the conversation.

## Running Tests

Thanks to the `pytest.ini` configuration, running tests is straightforward. From the root of the project, simply run:

```bash
uv run pytest
```
