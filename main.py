"""
Main Module

This module contains the main entry point for running graph visualization
and comparing pathfinding algorithms (BFS, Dijkstra, and A*).
"""

import random
from graph_utils import initialize_graph
from utils import run_all_algorithms
from compare_charts import plot_comparisons


def main():
    """
    Main function to initialize the graph, run algorithms, and visualize results.
    """
    place = "Gliwice, Poland"
    graph = initialize_graph(place)

    start_node = random.choice(list(graph.nodes))
    end_node = random.choice(list(graph.nodes))

    print(f"Start node: {start_node}")
    print(f"End node: {end_node}")

    results = run_all_algorithms(graph, start_node, end_node)

    plot_comparisons(results)


if __name__ == "__main__":
    main()
