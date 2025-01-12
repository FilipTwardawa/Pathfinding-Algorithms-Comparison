import pytest
from algorithms.a_star import AStarAlgorithm
from core.graph_processor import GraphProcessor
from core.graph_visualizer import GraphVisualizer
from core.graph_styler import GraphStyler
from utils.graph_initializer import initialize_graph
import asyncio
from unittest.mock import MagicMock


@pytest.mark.asyncio
async def test_a_star_execution():
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    algorithm = AStarAlgorithm(graph, visualizer, styler)

    GraphProcessor.initialize_edges(graph, styler)
    start_node, end_node = list(graph.nodes)[:2]
    await algorithm.execute(start_node, end_node, plot=False)

    assert (
        graph.nodes[end_node]["previous"] is not None
    ), "The path has not been designated correctly"


@pytest.mark.asyncio
async def test_a_star_with_delays():
    graph = initialize_graph("Gliwice, Poland")
    styler = GraphStyler()
    algorithm = AStarAlgorithm(graph, None, styler)
    start_node, end_node = list(graph.nodes)[:2]

    async def delayed_execute():
        await asyncio.sleep(0.5)
        await algorithm.execute(start_node, end_node, plot=False)

    await delayed_execute()

@pytest.mark.asyncio
async def test_a_star_with_mocked_styler():
    graph = initialize_graph("Gliwice, Poland")
    styler = MagicMock()
    algorithm = AStarAlgorithm(graph, None, styler)

    start_node, end_node = list(graph.nodes)[:2]
    await algorithm.execute(start_node, end_node, plot=False)

    assert styler.style_node.called, "Node styling has not been called"