import pytest
from algorithms.bfs import BFSAlgorithm
from core.graph_processor import GraphProcessor
from core.graph_visualizer import GraphVisualizer
from core.graph_styler import GraphStyler
from utils.graph_initializer import initialize_graph


@pytest.mark.asyncio
async def test_bfs_execution():
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
