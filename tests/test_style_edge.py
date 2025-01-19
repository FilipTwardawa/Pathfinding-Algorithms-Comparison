import networkx as nx
from core import GraphStyler


def test_style_edge_digraph():
    """Test styling of an edge in a directed graph.

    This test validates that the `GraphStyler.style_edge` method correctly
    applies specified styles to an edge in a directed graph (`nx.DiGraph`).

    Steps:
        1. Create a directed graph and add an edge.
        2. Apply styling to the edge using `GraphStyler.style_edge`.
        3. Assert that the applied styles (color, alpha, linewidth) are set correctly.

    Raises:
        AssertionError: If the applied styles do not match the expected values.
    """
    graph = nx.DiGraph()
    graph.add_edge(1, 2)
    GraphStyler.style_edge(graph, (1, 2), color="red", alpha=0.5, linewidth=2)

    assert graph.edges[1, 2]["color"] == "red"
    assert graph.edges[1, 2]["alpha"] == 0.5
    assert graph.edges[1, 2]["linewidth"] == 2


def test_style_edge_multidigraph():
    """Test styling of an edge in a multi-directed graph.

    This test ensures that the `GraphStyler.style_edge` method correctly
    applies styles to a specific edge in a multi-directed graph (`nx.MultiDiGraph`).

    Steps:
        1. Create a multi-directed graph and add multiple edges between nodes.
        2. Apply styling to a specific edge using `GraphStyler.style_edge`.
        3. Assert that the styles (color, alpha, linewidth) are correctly set for the target edge.

    Raises:
        AssertionError: If the styles of the edge do not match the expected values.
    """
    graph = nx.MultiDiGraph()
    graph.add_edge(1, 2, key=0)
    graph.add_edge(1, 2, key=1)
    GraphStyler.style_edge(graph, (1, 2, 1), color="blue", alpha=0.7, linewidth=3)

    assert graph.edges[1, 2, 1]["color"] == "blue"
    assert graph.edges[1, 2, 1]["alpha"] == 0.7
    assert graph.edges[1, 2, 1]["linewidth"] == 3


def test_style_node():
    """Test styling of a node in a directed graph.

    This test verifies that the `GraphStyler.style_node` method applies the specified
    style attributes to a node in a directed graph (`nx.DiGraph`).

    Steps:
        1. Create a directed graph and add a node.
        2. Apply styling to the node using `GraphStyler.style_node`.
        3. Assert that the style attribute (size) is correctly applied to the node.

    Raises:
        AssertionError: If the applied node style does not match the expected value.
    """
    graph = nx.DiGraph()
    graph.add_node(1)
    GraphStyler.style_node(graph, 1, size=20)

    assert graph.nodes[1]["size"] == 20
