"""
Test Algorithms Module

This module contains unit tests for various graph-related algorithms, including:
- BFS (Breadth-First Search)
- Dijkstra's Algorithm
- A* (A-star) Algorithm
"""

import random
from networkx.algorithms.components import connected_components
from graph_utils import initialize_graph, GraphProcessor, GraphStyler
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm
from chart_utils import generate_bar_chart


def test_initialize_graph():
    """
    Verifies that a graph is properly initialized from a given location.
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
    styler = GraphStyler()

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    components = list(connected_components(graph.to_undirected()))
    start = random.choice(list(components[0]))
    end = random.choice(list(components[0]))

    bfs = BFSAlgorithm(graph, None, styler)
    bfs.execute(start, end)
    assert graph.nodes[end]["visited"], "BFS failed to visit the end node."


def test_dijkstra_algorithm():
    """
    Tests Dijkstra's algorithm to find the shortest path.
    """
    graph = initialize_graph("Gliwice, Poland")
    styler = GraphStyler()

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    dijkstra = DijkstraAlgorithm(graph, None, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    dijkstra.execute(start, end)
    assert graph.nodes[end]["distance"] < float("inf"), "Dijkstra failed to find a path."


def test_astar_algorithm():
    """
    Tests the A* algorithm with a heuristic function.
    """
    graph = initialize_graph("Gliwice, Poland")
    styler = GraphStyler()

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    astar = AStarAlgorithm(graph, None, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    astar.execute(start, end)
    assert graph.nodes[end]["f_score"] < float("inf"), "A* failed to find a path."


def test_chart_generation():
    """
    Demonstrates chart generation with sample data.
    """
    results = {
        "BFS": {"cost": 10, "time": 0.02},
        "Dijkstra": {"cost": 8, "time": 0.01},
        "A*": {"cost": 7, "time": 0.015},
    }
    generate_bar_chart(results, "Algorithm Comparison", "Cost")
