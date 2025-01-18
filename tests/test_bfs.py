import pytest
from algorithms import BFSAlgorithm
from core import GraphProcessor, GraphVisualizer, GraphStyler
from utils import initialize_graph


@pytest.mark.asyncio
async def test_bfs_execution():
    """
    Tests the execution of the BFS (Breadth-First Search) algorithm in an asynchronous environment.

    This test:
    1. Initializes a graph based on the given location.
    2. Sets up the necessary visualizer and styler components.
    3. Initializes nodes and edges in the graph.
    4. Executes the BFS algorithm asynchronously to find a path between two nodes.
    5. Verifies if the end node has a designated 'previous' attribute, indicating a valid path.

    Args:
        None

    Raises:
        AssertionError: If the BFS algorithm does not correctly set the 'previous' attribute for the end node.
    """
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    algorithm = BFSAlgorithm(graph, visualizer, styler)

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    start_node, end_node = list(graph.nodes)[:2]
    await algorithm.execute(start_node, end_node, plot=False)

    assert (
            graph.nodes[end_node]["previous"] is not None
    ), "The path has not been designated correctly"
