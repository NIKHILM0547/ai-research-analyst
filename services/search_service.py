import os

from dotenv import load_dotenv

from tavily import TavilyClient


load_dotenv()

client = TavilyClient(

    api_key=os.getenv(

        "TAVILY_API_KEY"

    )

)


def search_business(query):

    response = client.search(

        query=query,

        max_results=3,

        search_depth="advanced",

        include_answer=True

    )

    return response["results"]