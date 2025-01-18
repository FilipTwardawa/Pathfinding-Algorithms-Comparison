import pytest
from algorithms import DijkstraAlgorithm
from core import GraphProcessor, GraphVisualizer, GraphStyler
from utils import initialize_graph
from time import time


@pytest.mark.asyncio
async def test_dijkstra_execution():
    """Test the execution of the Dijkstra algorithm.

    This test initializes a graph and executes the Dijkstra algorithm asynchronously
    to verify the correctness of the pathfinding process. The test ensures that
    a path is designated between a start and an end node.

    Steps:
        1. Initialize the graph for a given location ("Gliwice, Poland").
        2. Create instances of GraphVisualizer and GraphStyler.
        3. Use the DijkstraAlgorithm to compute the shortest path.
        4. Validate that the end node has a "previous" node set, indicating
           that a path has been designated.

    Raises:
        AssertionError: If the end node does not have a designated "previous" node.
    """
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
    """Test the performance of the Dijkstra algorithm.

    This test measures the execution time of the Dijkstra algorithm on a graph
    to ensure that it meets performance expectations for large graphs.

    Steps:
        1. Initialize the graph for a given location ("Gliwice, Poland").
        2. Execute the DijkstraAlgorithm to compute the shortest path between
           a start and an end node.
        3. Measure the elapsed time and ensure it is under the specified threshold.

    Raises:
        AssertionError: If the algorithm takes longer than 5 seconds to execute.
    """
    graph = initialize_graph("Gliwice, Poland")
    algorithm = DijkstraAlgorithm(graph, None, None)
    start_node, end_node = list(graph.nodes)[:2]

    start_time = time()
    algorithm.execute(start_node, end_node)
    elapsed_time = time() - start_time

    assert elapsed_time < 5.0, "Algorithm runs too slowly for large graph"
