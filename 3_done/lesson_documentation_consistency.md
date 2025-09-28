# Lesson Learned: Ensuring Documentation Consistency
[] copy the content of the planning, task, amd readme files back to their counterparts in _new_prj

## 1. Problem Summary

The project's core documents (`PLANNING.md`, `TASK.md`, and `README.md`) were inconsistent with each other and with the project's established tooling (`uv`).

1.  The iteration order in `PLANNING.md`, `TASK.md`, and `README.md` did not match the desired order specified in `idea.md`.
2.  The setup and usage instructions in `README.md` used generic `python` and `pip` commands instead of the project-standard `uv` commands.

This lesson provides the steps to bring all documentation into alignment.

## 2. Action Plan to Fix the Template Repository

Apply the following changes to the template repository to ensure consistency.

### 2.1. Update `PLANNING.md`

**Goal:** Correct the iteration order to prioritize Memory over Web Search.

**Action:** Swap the sections for Iteration 2 and Iteration 3.

**REPLACE THIS:**
```markdown
### Iteration 2: Adding Web Search
*   **Goal**: Give the agent its first tool to access external knowledge.
*   **Functionality**: The agent can answer questions about recent events or topics outside its training data.
*   **Testing**: Unit tests for the web search tool. User testing to confirm the agent uses the tool correctly.

### Iteration 3: Adding Memory
*   **Goal**: Make the agent stateful and conversational.
*   **Functionality**: The agent can remember information from earlier in the same conversation.
*   **Testing**: Unit tests for memory integration. User testing by asking the agent to recall previously mentioned facts.
```

**WITH THIS:**
```markdown
### Iteration 2: Adding Memory
*   **Goal**: Make the agent stateful and conversational.
*   **Functionality**: The agent can remember information from earlier in the same conversation.
*   **Testing**: Unit tests for memory integration. User testing by asking the agent to recall previously mentioned facts.

### Iteration 3: Adding Web Search
*   **Goal**: Give the agent its first tool to access external knowledge.
*   **Functionality**: The agent can answer questions about recent events or topics outside its training data.
*   **Testing**: Unit tests for the web search tool. User testing to confirm the agent uses the tool correctly.
```

### 2.2. Update `TASK.md`

**Goal:** Align the future task headers with the updated `PLANNING.md`.

**Action:** Swap the headers for Iteration 2 and Iteration 3.

**REPLACE THIS:**
```markdown
## Iteration 2: Adding Web Search (Future)
- [ ] ...

## Iteration 3: Adding Memory (Future)
- [ ] ...
```

**WITH THIS:**
```markdown
## Iteration 2: Adding Memory (Future)
- [ ] ...

## Iteration 3: Adding Web Search (Future)
- [ ] ...
```

### 2.3. Update `README.md`

**Goal:** Align setup/run commands with the `uv` toolchain and correct the iteration list.

**Action 1:** Update the environment setup commands.

**REPLACE THIS:**
```markdown
2.  **Create and activate a virtual environment:**
    ```bash
    # Navigate to the project directory
    cd ai-agent-mastery

    # Create a virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    # venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure your environment:**
```

**WITH THIS:**
```markdown
2.  **Create Environment and Install Dependencies:**
    This command first creates a virtual environment in a `.venv` folder and then installs the required Python packages into it.
    ```bash
    uv venv && uv pip install -r requirements.txt
    ```

3.  **Configure your environment:**
```

**Action 2:** Update the agent run command.

**REPLACE** `python cli.py` **WITH** `uv run cli.py`.

**Action 3:** Correct the future iteration list.

**REPLACE THIS:**
```markdown
- **Iteration 2:** Adding a web search tool.
- **Iteration 3:** Adding conversational memory.
```

**WITH THIS:**
```markdown
- **Iteration 2:** Adding conversational memory.
- **Iteration 3:** Adding a web search tool.
```

## 3. Summary

By applying these changes, the template repository's documentation will be internally consistent and aligned with the project's tooling, providing a clear and accurate starting point for new projects.
