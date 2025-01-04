"""
Comparison Charts Module

This module runs pathfinding algorithms (BFS, Dijkstra, A*) on a graph and generates
comparison charts to visualize the cost, execution time, path length, and number of visited nodes.
"""

from graph_utils import initialize_graph_with_distant_points, GraphStyler, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm
from chart_utils import generate_bar_chart


def run_algorithm(algorithm_class, graph, start_node, end_node, styler):
    """
    Runs a specified pathfinding algorithm on the given graph.

    Args:
        algorithm_class (class): The class of the algorithm to run (e.g., BFSAlgorithm).
        graph (networkx.Graph): The graph to run the algorithm on.
        start_node (int): The starting node.
        end_node (int): The target node.
        styler (GraphStyler): The object responsible for styling nodes and edges.

    Returns:
        tuple: The result of the algorithm execution.
    """
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    algorithm = algorithm_class(graph, None, styler)
    return algorithm.execute(start_node, end_node, plot=False)


def run_all_algorithms(graph, start_node, end_node, styler):
    """
    Runs BFS, Dijkstra, and A* algorithms and returns the results.

    Args:
        graph (networkx.Graph): The graph to run the algorithms on.
        start_node (int): The starting node.
        end_node (int): The target node.
        styler (GraphStyler): The object responsible for styling nodes and edges.

    Returns:
        dict: Results of all algorithms.
    """
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


def plot_comparisons(results):
    """
    Create bar charts for comparing the performance of algorithms.

    Args:
        results (dict): A dictionary containing the results of each algorithm.
    """
    generate_bar_chart(
        {algo: results[algo]["cost"] for algo in results}, "Cost Comparison", "Total Cost"
    )
    generate_bar_chart(
        {algo: results[algo]["time"] for algo in results}, "Execution Time Comparison", "Time (s)"
    )
    generate_bar_chart(
        {algo: results[algo]["depth"] for algo in results}, "Path Length Comparison", "Path Length"
    )
    generate_bar_chart(
        {algo: results[algo]["visited"] for algo in results}, "Visited Nodes Comparison", "Visited Nodes"
    )


def main():
    """
    Main function to initialize a graph, run pathfinding algorithms, and visualize comparisons.
    """
    graph, start_node, end_node = initialize_graph_with_distant_points("Warsaw, Poland")
    styler = GraphStyler()

    print(f"Start: {graph.nodes[start_node]['name']}, End: {graph.nodes[end_node]['name']}")

    results = run_all_algorithms(graph, start_node, end_node, styler)

    plot_comparisons(results)


if __name__ == "__main__":
    main()
