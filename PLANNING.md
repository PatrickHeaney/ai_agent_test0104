# AI Agent Baseline Project Planning

This document outlines the plan for creating a baseline starting point for new AI agents. The project will follow an iterative development model.

## Iteration 1: The Core Conversation Loop

*   **Goal**: Create the simplest possible, runnable agent.
*   **Functionality**: A user can start the terminal UI, have a basic conversation with the agent (no tools, no memory), and the agent will respond using the LLM.
*   **Testing**: Unit and user tests for agent/UI initialization to to validate.

## System Architecture (Iteration 1)

The initial architecture is minimal, focusing on the core conversation loop.

```
+-------------+
| Terminal UI |
+------+------+
       |
+------v------+
|   AI Agent  |
+-------------+
```

### Key Components (Iteration 1):

1.  **AI Agent**: Integrates with an LLM (configurable for local or cloud).
2.  **Terminal User Interface**: A basic command-line interface for interacting with the agent.

## Environment Configuration

The system will use environment variables for configuration:

```
# Base URL for the OpenAI compatible instance
LLM_BASE_URL=

# API key for your LLM provider
LLM_API_KEY=

# The LLM you want to use for the agents.
LLM_CHOICE=
```

## File Structure (Iteration 1)

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

## Testing Strategy

Unit tests will validate the initialization of the agent and the UI. User testing will involve running the agent and having a basic conversation.

---

## Future Iterations

### Iteration 2: Adding Memory
*   **Goal**: Make the agent stateful and conversational.
*   **Functionality**: The agent can remember information from earlier in the same conversation.
*   **Testing**: Unit tests for memory integration. User testing by asking the agent to recall previously mentioned facts.

### Iteration 3: Adding Web Search
*   **Goal**: Give the agent its first tool to access external knowledge.
*   **Functionality**: The agent can answer questions about recent events or topics outside its training data.
*   **Testing**: Unit tests for the web search tool. User testing to confirm the agent uses the tool correctly.
