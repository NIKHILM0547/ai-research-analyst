import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent

sys.path.append(str(ROOT))

from fastapi import FastAPI

from workflows.research_workflow import graph

from agents.compare_agent import compare_companies


app = FastAPI(

    title="AI Research Analyst API"

)


@app.get("/")

def home():

    return {

        "message": "AI Research Analyst API"

    }


@app.get("/analyze/{company}")

def analyze_company(

    company: str

):

    result = graph.invoke(

        {

            "company": company

        }

    )

    return {

        "company": company,

        "report": result["document"]

    }


@app.get("/compare")

def compare(

    company1: str,

    company2: str

):

    result = compare_companies(

        company1,

        company2

    )

    return {

        "comparison": result

    }