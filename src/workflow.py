"""
Workflow Definition for the Policy Sight AI.

This module defines the Directed Acyclic Graph (DAG) that orchestrates the
video compliance audit process. It connects the nodes (functional units)
using the StateGraph primitive from LangGraph.

Architecture:
    [START] -> [index_video_node] -> [audit_content_node] -> [END]
"""

from langgraph.graph import StateGraph, END

# Import the State Schema
from backend.src.graph.state import VideoAuditState

# Import the Functional Nodes
from backend.src.graph.nodes import (
    index_video_node,
    audit_content_node
)

def create_graph():
    """
    Constructs and compiles the LangGraph workflow.

    Returns:
        CompiledGraph: A runnable graph object ready for execution.
    """
    workflow = StateGraph(VideoAuditState)

    workflow.add_node("indexer", index_video_node)
    workflow.add_node("auditor", audit_content_node)

    workflow.set_entry_point("indexer")

    workflow.add_edge("indexer", "auditor")
    workflow.add_edge("auditor", END)

    graph_app = workflow.compile()

    return graph_app


# Expose the runnable graph for import by the API or CLI
app = create_graph()
