import pytest
from core import GraphVisualizer, GraphStyler, PathReconstructor
from algorithms import DijkstraAlgorithm
from utils import initialize_graph


@pytest.mark.asyncio
async def test_full_pipeline_integration():
    """
    Test the integration of the graph algorithm, visualizer, and path reconstructor.

    This test performs the following steps:
    1. Initializes a graph based on a geographic location.
    2. Executes the Dijkstra algorithm to find the shortest path between two nodes.
    3. Reconstructs the path and generates a visual representation.
    4. Verifies the correctness of the path and visualization output.

    Args:
        None

    Raises:
        AssertionError: If the path reconstruction or visualization is incorrect.
    """
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    algorithm = DijkstraAlgorithm(graph, visualizer, styler)
    reconstructor = PathReconstructor(graph, visualizer, styler)
    start_node, end_node = list(graph.nodes)[:2]

    # Running the algorithm
    await algorithm.execute(start_node, end_node, plot=True)

    # Path reconstruction
    await reconstructor.reconstruct_path(start_node, end_node, plot=True)

    # Checking the results
    assert (
            graph.nodes[end_node]["previous"] is not None
    ), "The path has not been designated correctly"
    assert len(visualizer.frames) > 0, "Visualization has not been generated"
