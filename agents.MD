# Project Agents

This document outlines the AI agents and their capabilities within the `ollamatest` project.

## Search Assistant Agent

The primary agent in this project is a CLI-based assistant designed to provide real-time information by bridging the gap between a local LLM and the web.

### Core Configuration
- **Model**: `llama3.1:8b` (running via Ollama)
- **Interface**: Command Line Interface (CLI)
- **Backend**: Ollama Chat API (`/api/chat`)

### Role & Persona
The agent is configured as a **Helpful Assistant** with the following system instructions:
> "You are a helpful assistant that can search the web for information."

It is also provided with real-time context regarding the current date and time to ensure accuracy in time-sensitive queries.

### Capabilities & Tools
The agent has access to external tools to extend its knowledge beyond its training data:

| Tool Name | Description | Parameters | Implementation |
|-----------|-------------|------------|----------------|
| `web_search` | Searches the web for information using DuckDuckGo. | `query` (string) | `agent_tools.py` using `DDGS` |

### Workflow
1. **User Input**: The user interacts via the CLI.
2. **Tool Detection**: The LLM determines if a tool call (like `web_search`) is necessary.
3. **Execution**: If a tool is called, the `handle_tool_calls` function executes the search and returns the top 3 results.
4. **Final Response**: The LLM synthesizes the search results into a natural language response for the user.

### Module Structure & Tool Logic

To maintain a clean separation of concerns, all tool-related logic resides in the `agent_tools.py` module.

- **`TOOLS_DEFINITIONS`**: A list of JSON objects that define the tool's interface (name, description, parameters) for the LLM.
- **`handle_tool_calls`**: Acts as a **function router**. It iterates through the tool calls requested by the LLM and dispatches them to the appropriate implementation.
- **Function Implementations**: The actual logic for each tool (e.g., `web_search`) is implemented as a standalone function within this module.

### How to Run
To start a conversation with the agent, run:
```bash
python app.py
```
Type `quit`, `exit`, or `bye` to end the session.
