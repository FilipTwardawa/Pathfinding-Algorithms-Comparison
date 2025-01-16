import pytest
from core import GraphVisualizer, GraphStyler, PathReconstructor
from algorithms import DijkstraAlgorithm
from utils import initialize_graph


@pytest.mark.asyncio
async def test_full_pipeline_integration():
    """Checks the integration of the algorithm, visualizer and path reconstructor."""
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
