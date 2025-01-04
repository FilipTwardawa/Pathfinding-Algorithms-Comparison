"""
Unit tests for pathfinding algorithms and graph utilities.
"""

import random
from networkx.algorithms.components import connected_components
from graph_utils import initialize_graph, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm
from chart_utils import plot_bar_chart


def test_initialize_graph():
    """
    Tests graph initialization to ensure nodes and edges exist.
    """
    graph = initialize_graph("Gliwice, Poland")
    assert graph is not None, "Graph not initialized."
    assert len(graph.nodes) > 0, "Graph must have nodes."
    assert len(graph.edges) > 0, "Graph must have edges."


def test_bfs_algorithm():
    """
    Tests the BFS algorithm on a sample graph.
    """
    graph = initialize_graph("Gliwice, Poland")
    GraphProcessor.initialize_nodes(graph)

    components = list(connected_components(graph.to_undirected()))
    start = random.choice(list(components[0]))
    end = random.choice(list(components[0]))

    bfs = BFSAlgorithm(graph)
    path, _, _, _, _ = bfs.execute(start, end)
    assert end in path, "BFS failed to visit the end node."


def test_dijkstra_algorithm():
    """
    Tests Dijkstra's algorithm to find the shortest path.
    """
    graph = initialize_graph("Gliwice, Poland")
    GraphProcessor.initialize_nodes(graph)

    dijkstra = DijkstraAlgorithm(graph)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    path, cost, _, _, _ = dijkstra.execute(start, end)
    assert cost < float("inf"), "Dijkstra failed to find a path."
    assert end in path, "Dijkstra failed to include the end node in the path."


def test_astar_algorithm():
    """
    Tests the A* algorithm with a heuristic function to ensure a valid path is found.
    """
    graph = initialize_graph("Gliwice, Poland")
    GraphProcessor.initialize_nodes(graph)

    for node in graph.nodes:
        graph.nodes[node]["x"] = random.uniform(0, 1)
        graph.nodes[node]["y"] = random.uniform(0, 1)

    astar = AStarAlgorithm(graph)
    path, cost, _, _, _ = astar.execute(start=list(graph.nodes)[0], end=list(graph.nodes)[-1])

    assert cost < float("inf"), "A* failed to find a path."
    assert len(path) > 0, "A* failed to return a valid path."


def test_chart_generation():
    """
    Tests the chart generation utility to ensure bar charts are created correctly.
    """
    results = {
        "BFS": {"cost": 10, "time": 0.1},
        "Dijkstra": {"cost": 8, "time": 0.05},
        "A*": {"cost": 9, "time": 0.07},
    }
    plot_bar_chart(results["BFS"], "Cost Comparison", "Total Cost")
    plot_bar_chart(results["Dijkstra"], "Execution Time Comparison", "Time (seconds)")
