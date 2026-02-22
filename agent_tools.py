"""
This module contains the tool definitions and logic for the AI agent.

It includes:
- TOOLS_DEFINITIONS: JSON schemas for the LLM to understand available tools.
- handle_tool_calls: A router function that executes requested tool calls.
- Tool implementations: Standalone functions that perform the actual tasks (e.g., web_search).
"""

from ddgs import DDGS

# Tool Call Handler
def handle_tool_calls(tool_calls):
    """
    Processes a list of tool calls from the LLM and routes them to their respective functions.

    Args:
        tool_calls (list): A list of tool call objects from the Ollama API response.

    Returns:
        list: A list of tool response messages to be sent back to the LLM.
    """
    messages = []

    for tool_call in tool_calls:
        function_call = tool_call["function"]

        if function_call["name"] == "web_search":
            print("Assistant: Searching the web for ", function_call["arguments"]["query"])
            query = function_call["arguments"]["query"]
            results = web_search(query)
            messages.append({
                "role" : "tool",
                "tool_name" : "web_search",
                "content" : results
            })

        else:
            messages.append({
                "role" : "tool",
                "tool_name" : function_call["name"],
                "content" : "Tool not found"
            })
    return messages

# Tool definitions
TOOLS_DEFINITIONS = [
    {
        "type" : "function",
        "function" : {
            "name" : "web_search",
            "description" : "Search the web for information",
            "parameters" : {
                "type" : "object",
                "properties" : {
                    "query" : {"type" : "string", "description" : "The query to search the web for"}
                }
            },
            "required" : ["query"]
        }
    }
]


# Tool functions
def web_search(query):
    """
    Performs a web search using DuckDuckGo and returns a formatted string of results.

    Args:
        query (str): The search query.

    Returns:
        str: A newline-separated string containing titles, snippets, and links for the top 3 results.
    """
    # print(f"Searching the web for: {query}")
    results = DDGS().text(query, max_results=3)
    return "\n".join(f"[{result['title']}] {result['body']} [{result['href']}]" for result in results)
