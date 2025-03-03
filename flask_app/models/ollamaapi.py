import requests
import json

def chat_with_ollama(user_message):
    url = "http://localhost:11434/api/chat"  # Change if API URL differs
    payload = {
        "model": "Mistral",
        "Messages": [{"role": "user", "content": user_message}]
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json().get("message", {}).get("content", "No response")
    else:
        return f"Error: {response.status_code} - {response.text}"
