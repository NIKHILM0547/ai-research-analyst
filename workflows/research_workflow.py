from typing import TypedDict

from agents.planner_agent import create_research_plan

from agents.search_agent import perform_search

from agents.validator_agent import validate_findings

from agents.filter_agent import filter_findings

from agents.source_scorer_agent import score_sources

from agents.analyst_agent import analyze

from agents.writer_agent import create_document

from langgraph.graph import StateGraph


class ResearchState(TypedDict):

    company: str

    plan: list

    findings: list

    report: str

    document: str


def planner_node(state):

    state["plan"] = create_research_plan(

        state["company"]

    )

    return state


def search_node(state):

    state["findings"] = perform_search(

        state["plan"]

    )

    return state


def validator_node(state):

    state["findings"] = validate_findings(

        state["findings"]

    )

    return state


def filter_node(state):

    state["findings"] = filter_findings(

        state["findings"]

    )

    return state


def scorer_node(state):

    state["findings"] = score_sources(

        state["findings"]

    )

    return state


def analyst_node(state):

    state["report"] = analyze(

        state["findings"]

    )

    return state


def writer_node(state):

    state["document"] = create_document(

        state["report"]

    )

    return state


builder = StateGraph(

    ResearchState

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

graph = builder.compile()