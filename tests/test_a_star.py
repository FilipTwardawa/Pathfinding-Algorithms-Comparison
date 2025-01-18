import pytest
from unittest.mock import MagicMock
import asyncio
from algorithms import AStarAlgorithm
from core import GraphProcessor, GraphVisualizer, GraphStyler
from utils import initialize_graph


@pytest.mark.asyncio
async def test_a_star_execution():
    """
    Test the execution of the A* algorithm.

    This test verifies that the A* algorithm can correctly designate
    the path between two nodes in a graph.

    Steps:
        1. Initialize the graph for "Gliwice, Poland".
        2. Set up the GraphVisualizer and GraphStyler.
        3. Execute the A* algorithm between the start and end nodes.
        4. Assert that the end node has a designated "previous" node.

    Raises:
        AssertionError: If the path is not designated correctly.
    """
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    algorithm = AStarAlgorithm(graph, visualizer, styler)

    GraphProcessor.initialize_edges(graph, styler)
    start_node, end_node = list(graph.nodes)[:2]
    await algorithm.execute(start_node, end_node, plot=False)

    assert graph.nodes[end_node]["previous"] is not None, "The path has not been designated correctly"


@pytest.mark.asyncio
async def test_a_star_with_delays():
    """
    Test the A* algorithm with delayed execution.

    This test verifies that the algorithm handles delays during execution
    correctly without raising exceptions.

    Steps:
        1. Initialize the graph for "Gliwice, Poland".
        2. Define an asynchronous delay before executing the algorithm.
        3. Execute the algorithm between the start and end nodes.

    Raises:
        AssertionError: If an exception occurs during delayed execution.
    """
    graph = initialize_graph("Gliwice, Poland")
    styler = GraphStyler()
    algorithm = AStarAlgorithm(graph, None, styler)
    start_node, end_node = list(graph.nodes)[:2]

    async def delayed_execute():
        """Introduce a delay before executing the algorithm."""
        await asyncio.sleep(0.5)
        await algorithm.execute(start_node, end_node, plot=False)

    await delayed_execute()


@pytest.mark.asyncio
async def test_a_star_with_mocked_styler():
    """
    Test the A* algorithm using a mocked GraphStyler.

    This test verifies that the algorithm interacts correctly with
    the GraphStyler by checking if the style_node method is called.

    Steps:
        1. Initialize the graph for "Gliwice, Poland".
        2. Mock the GraphStyler.
        3. Execute the algorithm between the start and end nodes.
        4. Assert that the style_node method was called.

    Raises:
        AssertionError: If the style_node method is not called.
    """
    graph = initialize_graph("Gliwice, Poland")
    styler = MagicMock()
    algorithm = AStarAlgorithm(graph, None, styler)

    start_node, end_node = list(graph.nodes)[:2]
    await algorithm.execute(start_node, end_node, plot=False)

    assert styler.style_node.called, "Node styling has not been called"
