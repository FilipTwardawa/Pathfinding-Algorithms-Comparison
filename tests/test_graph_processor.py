from core.graph_processor import GraphProcessor
from core.graph_styler import GraphStyler
from utils.graph_initializer import initialize_graph


def test_initialize_nodes():
    graph = initialize_graph("Gliwice, Poland")
    GraphProcessor.initialize_nodes(graph)

    # Sprawdź, czy wszystkie węzły są zainicjalizowane
    for node in graph.nodes:
        assert (
            graph.nodes[node].get("visited") is False
        ), f"Node {node} was not properly initialized"
        assert graph.nodes[node].get("distance") == float(
            "inf"
        ), f"The distance of the node {node} was not properly initialized"



def test_initialize_edges():
    graph = initialize_graph("Gliwice, Poland")
    styler = GraphStyler()
    GraphProcessor.initialize_edges(graph, styler)

    for edge in graph.edges:
        assert (
            "color" in graph.edges[edge]
        ), "Edge styling was not applied correctly"
