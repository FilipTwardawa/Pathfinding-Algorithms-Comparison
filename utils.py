"""
Utility functions for running pathfinding algorithms.
"""

from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm
from graph_utils import GraphProcessor


def run_all_algorithms(graph, start_node, end_node):
    """
    Runs BFS, Dijkstra, and A* algorithms and returns the results.

    Args:
        graph (networkx.Graph): The graph to run the algorithms on.
        start_node (int): The starting node.
        end_node (int): The target node.

    Returns:
        dict: Results of all algorithms.
    """
    GraphProcessor.initialize_nodes(graph)

    results = {}
    for algo_class, algo_name in [
        (BFSAlgorithm, "BFS"),
        (DijkstraAlgorithm, "Dijkstra"),
        (AStarAlgorithm, "A*"),
    ]:
        print(f"Running {algo_name}...")
        algorithm = algo_class(graph)
        results[algo_name] = algorithm.execute(start_node, end_node)
        print(f"{algo_name} completed.")

    return results
