My idea for this project is to create baseline starting point for new AI agents.

## Iterative Development Plan

The project will follow an iterative development model. Each iteration delivers a runnable, testable version of the agent with increasing capabilities, ensuring continuous feedback and progress.

### Iteration 1: The Core Conversation Loop
*   **Goal**: Create the simplest possible, runnable agent.
*   **Functionality**: A user can start the terminal UI, have a basic conversation with the agent (no tools, no memory), and the agent will respond using the LLM.
*   **Testing**: Unit and user tests for agent/UI initialization to to validate.

### Iteration 2: Adding Memory
*   **Goal**: Make the agent stateful and conversational.
*   **Functionality**: The agent can remember information from earlier in the same conversation.
*   **Testing**: Unit tests for the `mem0` integration points. User testing by asking the agent to recall previously mentioned facts.

### Iteration 3: Adding Web Search
*   **Goal**: Give the agent its first tool to access external knowledge.
*   **Functionality**: The agent can answer questions about recent events or topics outside its training data.
*   **Testing**: Unit tests for the web search tool. User testing to confirm the agent uses the tool correctly.

My list of Local MCP Servers includes
[] Brave Search - `https://github.com/brave/brave-search-mcp-server`
[] Manage local files - `https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem`
[] Manage local git repositories - `https://github.com/modelcontextprotocol/servers/tree/main/src/git`
[] Crawl4AI RAG - `https://github.com/coleam00/mcp-crawl4ai-rag`
