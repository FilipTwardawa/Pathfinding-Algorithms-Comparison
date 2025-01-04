"""
Comparison Module

This module compares the performance of different pathfinding algorithms.
"""

from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm
from graph_utils import initialize_graph, GraphProcessor, GraphStyler


def run_algorithm(algorithm_class, graph, start_node, end_node, styler):
    """
    Runs a single algorithm on a graph.

    Args:
        algorithm_class: The algorithm class to be instantiated.
        graph (networkx.Graph): The graph to run the algorithm on.
        start_node (int): The starting node.
        end_node (int): The target node.
        styler (GraphStyler): The object responsible for styling nodes and edges.

    Returns:
        tuple: The result of the algorithm execution.
    """
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    algorithm = algorithm_class(graph)
    return algorithm.execute(start_node, end_node)


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
    styler = GraphStyler()
    results = {}

    for algo_class, algo_name in [
        (BFSAlgorithm, "BFS"),
        (DijkstraAlgorithm, "Dijkstra"),
        (AStarAlgorithm, "A*"),
    ]:
        print(f"Running {algo_name}...")
        results[algo_name] = run_algorithm(algo_class, graph, start_node, end_node, styler)
        print(f"{algo_name} completed.")

    return results


def main():
    """
    Main function to initialize the graph and run comparisons.
    """
    place = "Gliwice, Poland"
    graph = initialize_graph(place)

    start_node = list(graph.nodes)[0]
    end_node = list(graph.nodes)[-1]

    results = run_all_algorithms(graph, start_node, end_node)

    for algo_name, result in results.items():
        path, cost, time_taken, depth, visited = result
        print(f"{algo_name} results:")
        print(f"  Path: {path}")
        print(f"  Cost: {cost}")
        print(f"  Time: {time_taken:.4f} seconds")
        print(f"  Depth: {depth}")
        print(f"  Visited Nodes: {visited}")


if __name__ == "__main__":
    main()
