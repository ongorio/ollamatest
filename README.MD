# Ollama Search Assistant

A Python-based CLI application that allows users to interact with local LLMs via Ollama, enhanced with real-time web search capabilities.

## Features

- **Local LLM Integration**: Uses Ollama to run models like `llama3.1:8b` locally.
- **Web Search Tool**: Automatically searches the web using DuckDuckGo when the LLM needs real-time information.
- **Persistent Conversation**: Maintains chat history during the session.
- **Modular Design**: Clear separation between the chat loop and tool execution logic.

## Prerequisites

- [Ollama](https://ollama.com/) installed and running.
- Python 3.8+
- The `llama3.1:8b` model pulled:
  ```bash
  ollama pull llama3.1:8b
  ```

## Installation

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main application:
```bash
python app.py
```

Type your questions in the CLI. The assistant will decide whether to answer from its training data or perform a web search to provide up-to-date information.

To exit, type `quit`, `exit`, or `bye`.

## Project Structure

- `app.py`: Main entry point, handles the chat loop and Ollama API communication.
- `agent_tools.py`: Contains tool definitions, the tool router, and actual tool implementations.
- `agents.MD`: Documentation of the agent's roles, tools, and architecture.

## License

MIT
