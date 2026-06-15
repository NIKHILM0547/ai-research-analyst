import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key
)


def ask_gemini(prompt):

    try:

        response = client.models.generate_content(

            model="gemini-2.0-flash-lite",

            contents=prompt

        )

        return response.text

    except Exception as e:

        print("\nGemini Error:")

        print(e)

        return None