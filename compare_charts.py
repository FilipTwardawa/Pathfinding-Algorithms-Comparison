"""
Comparison Charts Module

This module generates comparison charts for BFS, Dijkstra, and A* algorithms.
"""

from utils import run_all_algorithms
from chart_utils import generate_bar_chart
from graph_utils import initialize_graph_with_distant_points


def plot_comparisons(results):
    """
    Create bar charts for comparing the performance of algorithms.

    Args:
        results (dict): A dictionary containing the results of each algorithm.
    """
    generate_bar_chart({algo: results[algo][1] for algo in results},
                       "Cost Comparison", "Total Cost")
    generate_bar_chart({algo: results[algo][2] for algo in results},
                       "Execution Time Comparison", "Time (s)")
    generate_bar_chart({algo: results[algo][3] for algo in results},
                       "Path Length Comparison", "Path Length")
    generate_bar_chart({algo: results[algo][4] for algo in results},
                       "Visited Nodes Comparison", "Visited Nodes")


def main():
    """
    Main function to initialize a graph, run pathfinding algorithms, and visualize comparisons.
    """
    graph, start_node, end_node = initialize_graph_with_distant_points("Warsaw, Poland")

    results = run_all_algorithms(graph, start_node, end_node)

    plot_comparisons(results)


if __name__ == "__main__":
    main()
