from core import GraphProcessor, GraphStyler
from utils import initialize_graph


def test_initialize_nodes():
    """
    Tests the initialization of nodes in a graph.

    This function initializes a graph for a given location ("Gliwice, Poland") and applies
    the `initialize_nodes` method from the `GraphProcessor`. It then verifies:
    1. Each node has its "visited" attribute set to `False`.
    2. Each node has its "distance" attribute set to infinity (`float("inf")`).

    Raises:
        AssertionError: If any node is not properly initialized with the expected attributes.
    """
    graph = initialize_graph("Gliwice, Poland")
    GraphProcessor.initialize_nodes(graph)

    for node in graph.nodes:
        assert (
                graph.nodes[node].get("visited") is False
        ), f"Node {node} was not properly initialized"
        assert graph.nodes[node].get("distance") == float(
            "inf"
        ), f"The distance of the node {node} was not properly initialized"


def test_initialize_edges():
    """
    Tests the initialization and styling of edges in a graph.

    This function initializes a graph for a given location ("Gliwice, Poland"), creates a
    `GraphStyler` instance, and applies the `initialize_edges` method from the `GraphProcessor`.
    It then verifies that each edge in the graph has been correctly styled with a "color" attribute.

    Raises:
        AssertionError: If any edge does not have the "color" attribute applied correctly.
    """
    graph = initialize_graph("Gliwice, Poland")
    styler = GraphStyler()
    GraphProcessor.initialize_edges(graph, styler)

    for edge in graph.edges:
        assert (
                "color" in graph.edges[edge]
        ), "Edge styling was not applied correctly"
