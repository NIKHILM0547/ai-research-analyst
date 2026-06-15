import os

from dotenv import load_dotenv

from tavily import TavilyClient


load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

client = TavilyClient(api_key=api_key)


def search_business(query):

    response = client.search(

        query=query,

        max_results=5

    )

    return response["results"]