import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MOCK_API_KEY")

url = "http://localhost:8000/chat"


def ask_ai(prompt):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mock-model",
        "prompt": prompt
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload
    )

    if response.ok:
        data = response.json()
        return data["output"]

    raise Exception(
        f"API request failed: {response.status_code}"
    )