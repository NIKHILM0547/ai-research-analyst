from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.planner_agent import create_research_plan
from agents.search_agent import perform_search
from agents.validator_agent import validate_findings
from agents.filter_agent import filter_findings
from agents.source_scorer_agent import score_sources
from agents.analyst_agent import analyze
from agents.writer_agent import create_document

from services.cache_service import get_cache
from services.cache_service import save_cache

from services.report_service import save_report


class ResearchState(TypedDict, total=False):

    company: str

    plan: list

    findings: list

    report: str

    document: str

    cached: bool


# ---------------- CACHE ----------------


def cache_node(state):

    print("\nChecking cache...\n")

    company = state["company"]

    cached_document = get_cache(company)

    if cached_document:

        state["document"] = cached_document

        state["cached"] = True

    else:

        state["cached"] = False

    return state


# ---------------- PLANNER ----------------


def planner_node(state):

    if state.get("cached"):

        return state

    state["plan"] = create_research_plan(

        state["company"]

    )

    return state


# ---------------- SEARCH ----------------


def search_node(state):

    if state.get("cached"):

        return state

    state["findings"] = perform_search(

        state["plan"]

    )

    return state


# ---------------- VALIDATOR ----------------


def validator_node(state):

    if state.get("cached"):

        return state

    state["findings"] = validate_findings(

        state["findings"]

    )

    return state


# ---------------- FILTER ----------------


def filter_node(state):

    if state.get("cached"):

        return state

    state["findings"] = filter_findings(

        state["findings"]

    )

    return state


# ---------------- SOURCE SCORER ----------------


def scorer_node(state):

    if state.get("cached"):

        return state

    state["findings"] = score_sources(

        state["findings"]

    )

    return state


# ---------------- ANALYST ----------------


def analyst_node(state):

    if state.get("cached"):

        return state

    state["report"] = analyze(

        state["findings"]

    )

    return state


# ---------------- WRITER ----------------


def writer_node(state):

    company = state["company"]

    # Cache hit

    if state.get("cached"):

        document = state.get("document")

        if document:

            save_report(

                company,

                document

            )

        return state

    report = state.get(

        "report",

        ""

    )

    if not report:

        report = "Report generation failed."

    document = create_document(

        report

    )

    state["document"] = document

    if report != "Report generation failed.":

        save_cache(

            company,

            document

        )

        save_report(

            company,

            document

        )

    return state


# ---------------- BUILD GRAPH ----------------


builder = StateGraph(

    ResearchState

)

builder.add_node(

    "cache",

    cache_node

)

builder.add_node(

    "planner",

    planner_node

)

builder.add_node(

    "search",

    search_node

)

builder.add_node(

    "validator",

    validator_node

)

builder.add_node(

    "filter",

    filter_node

)

builder.add_node(

    "scorer",

    scorer_node

)

builder.add_node(

    "analyst",

    analyst_node

)

builder.add_node(

    "writer",

    writer_node

)


builder.set_entry_point(

    "cache"

)


builder.add_edge(

    "cache",

    "planner"

)

builder.add_edge(

    "planner",

    "search"

)

builder.add_edge(

    "search",

    "validator"

)

builder.add_edge(

    "validator",

    "filter"

)

builder.add_edge(

    "filter",

    "scorer"

)

builder.add_edge(

    "scorer",

    "analyst"

)

builder.add_edge(

    "analyst",

    "writer"

)

builder.add_edge(

    "writer",

    END

)


graph = builder.compile()