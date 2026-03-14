
import requests
from config import OPENAI_API

def generate_report(data):

    url = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {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}",
        "Content-Type": "application/json"
    }

    payload = {

        "model":"gpt-4o-mini",

        "messages":[
            {
                "role":"system",
                "content":"You are a cyber threat intelligence analyst generating OSINT investigation reports."
            },
            {
                "role":"user",
                "content":str(data)
            }
        ]

    }

    try:

        r = requests.post(url,headers=headers,json=payload)

        result = r.json()

        return result["choices"][0]["message"]["content"]

    except:

        return "AI report generation failed"
