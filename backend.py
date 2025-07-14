import requests

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-r1:free"

def get_bot_reply(user_msg):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Tkinter Chatbot"
    }

    data = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_msg}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        if response.status_code != 200:
            return f"⚠️ Request Error: {response.status_code}\n{response.text}"
        return response.json()['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"⚠️ Error: {str(e)}"