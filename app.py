import requests
from datetime import datetime
from agent_tools import TOOLS_DEFINITIONS, handle_tool_calls

MODEL = "llama3.1:8b"


def chat_with_agent(model, prompt, messages):
    url = "http://localhost:11434/api/chat"

    messages.append({
        "role" : "system",
        "content" : f"You are a helpful assistant that can search the web for information. The current Date and Time is {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}."
    })

    messages.append({
        "role" : "user",
        "content" : prompt
    })

    payload = {
        "model" : model,
        "stream" : False,
        "tools" : TOOLS_DEFINITIONS,
        "messages" : messages
    }

    response = requests.post(url, json=payload).json()
    print("Response: ", response)
    message = response["message"]

    if message.get("tool_calls"):
        messages.append(message)

        # Handle tool calls
        messages.extend(handle_tool_calls(message["tool_calls"]))  
        
        final_payload = {
            "model" : model,
            "stream" : False,
            # "tools" : tools,
            "messages" : messages
        }

        final_response = requests.post(url, json=final_payload).json()
        message = final_response["message"]
        messages.append({
            "role" : "assistant",
            "content" : message["content"].strip()
        })
        print("Assistant: ", message["content"].strip())
    else:
        messages.append({
            "role" : "assistant",
            "content" : message["content"].strip()
        })
        print("Assistant: ", message["content"].strip())

    return messages

conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye"]:
        break
    conversation_history = chat_with_agent(MODEL, user_input, conversation_history)
