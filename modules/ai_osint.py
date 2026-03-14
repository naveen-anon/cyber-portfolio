import requests

API_KEY = "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"

def ask_ai(question):

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role":"system","content":"You are a cyber OSINT assistant"},
            {"role":"user","content":question}
        ]
    }

    r = requests.post(url, headers=headers, json=data)

    try:
        return r.json()["choices"][0]["message"]["content"]
    except:
        return "AI error"
