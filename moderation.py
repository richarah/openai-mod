import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    print("OPENAI_API_KEY environment variable is not set")
    exit(1)

text = input("Enter text to moderate: ")

payload = {
    "prompt": "",
    "max_tokens": 0,
    "temperature": 0,
    "threshold": 0.5,
    "censor": "curse",
    "input": text
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}",
}

response = requests.post("https://api.openai.com/v1/moderations", json=payload, headers=headers)

print(json.dumps(response.json(), indent=4))
