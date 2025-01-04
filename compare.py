"""
Comparison Module

This module compares the performance of different pathfinding algorithms.
"""

from utils import run_all_algorithms
from graph_utils import initialize_graph


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
