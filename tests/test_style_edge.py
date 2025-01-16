import networkx as nx
from core import GraphStyler


def test_style_edge_digraph():
    graph = nx.DiGraph()
    graph.add_edge(1, 2)
    GraphStyler.style_edge(graph, (1, 2), color="red", alpha=0.5, linewidth=2)

    assert graph.edges[1, 2]["color"] == "red"
    assert graph.edges[1, 2]["alpha"] == 0.5
    assert graph.edges[1, 2]["linewidth"] == 2


def test_style_edge_multidigraph():
    graph = nx.MultiDiGraph()
    graph.add_edge(1, 2, key=0)
    graph.add_edge(1, 2, key=1)
    GraphStyler.style_edge(graph, (1, 2, 1), color="blue", alpha=0.7, linewidth=3)

    assert graph.edges[1, 2, 1]["color"] == "blue"
    assert graph.edges[1, 2, 1]["alpha"] == 0.7
    assert graph.edges[1, 2, 1]["linewidth"] == 3


def test_style_node():
    graph = nx.DiGraph()
    graph.add_node(1)
    GraphStyler.style_node(graph, 1, size=20)

    assert graph.nodes[1]["size"] == 20
