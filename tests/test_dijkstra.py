import pytest
from algorithms.dijkstra import DijkstraAlgorithm
from core.graph_processor import GraphProcessor
from core.graph_visualizer import GraphVisualizer
from core.graph_styler import GraphStyler
from utils.graph_initializer import initialize_graph
from time import time


@pytest.mark.asyncio
async def test_dijkstra_execution():
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    algorithm = DijkstraAlgorithm(graph, visualizer, styler)

    GraphProcessor.initialize_edges(graph, styler)
    start_node, end_node = list(graph.nodes)[:2]
    await algorithm.execute(start_node, end_node, plot=False)

    assert (
        graph.nodes[end_node]["previous"] is not None
    ), "The path has not been designated correctly"


@pytest.mark.performance
def test_dijkstra_performance():
    graph = initialize_graph("Gliwice, Poland")
    algorithm = DijkstraAlgorithm(graph, None, None)
    start_node, end_node = list(graph.nodes)[:2]

    start_time = time()
    algorithm.execute(start_node, end_node)
    elapsed_time = time() - start_time

    assert elapsed_time < 5.0, "Algorithm runs too slowly for large graph"
