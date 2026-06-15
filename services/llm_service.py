import requests


OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = "qwen3:4b"


def ask_llm(prompt):

    response = requests.post(

        OLLAMA_URL,

        json={

            "model": MODEL,

            "prompt": prompt,

            "stream": False

        }

    )

    response.raise_for_status()

    data = response.json()

    return data["response"]