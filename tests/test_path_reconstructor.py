import pytest
from core import GraphProcessor, PathReconstructor, GraphVisualizer, GraphStyler
from utils import initialize_graph


@pytest.mark.asyncio
async def test_path_reconstruction():
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    reconstructor = PathReconstructor(graph, visualizer, styler)

    start_node, end_node = list(graph.nodes)[:2]
    graph.nodes[end_node]["previous"] = start_node

    graph.add_edge(start_node, end_node, key=0, weight=1)

    GraphProcessor.initialize_edges(graph, styler)

    await reconstructor.reconstruct_path(start_node, end_node, plot=True)
    assert len(
        visualizer.frames) > 0, "Path visualization not generated"
