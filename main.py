"""
Main Module

This module contains the main entry point for running graph visualization
and comparing pathfinding algorithms (BFS, Dijkstra, and A*).
"""

import random
import matplotlib.pyplot as plt
from graph_utils import initialize_graph, GraphStyler, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm


def plot_comparisons(results):
    """
    Create enhanced bar charts for cost and execution time comparisons.

    Args:
        results (dict): A dictionary containing algorithm results (cost, time, etc.).
    """
    # Extract data
    algorithms = list(results.keys())
    costs = [results[algo]["cost"] for algo in algorithms]
    times = [results[algo]["time"] for algo in algorithms]

    # Plot costs
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, costs, color=["blue", "green", "orange"])
    plt.title("Cost Comparison", fontsize=16)
    plt.ylabel("Total Cost", fontsize=12)
    plt.xlabel("Algorithms", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Add values on top of bars
    for bar_segment in bars:  # Replaced "bar" with "bar_segment"
        plt.text(
            bar_segment.get_x() + bar_segment.get_width() / 2,
            bar_segment.get_height(),
            f"{bar_segment.get_height():.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.show()

    # Plot execution times
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, times, color=["blue", "green", "orange"])
    plt.title("Execution Time Comparison", fontsize=16)
    plt.ylabel("Time (seconds)", fontsize=12)
    plt.xlabel("Algorithms", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Add values on top of bars
    for bar_segment in bars:  # Replaced "bar" with "bar_segment"
        plt.text(
            bar_segment.get_x() + bar_segment.get_width() / 2,
            bar_segment.get_height(),
            f"{bar_segment.get_height():.4f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    plt.show()


def main():
    """
    Main function to initialize the graph, run algorithms, and visualize results.
    """
    # Ustawienie miejsca, dla którego generujemy graf
    place = "Gliwice, Poland"
    graph = initialize_graph(place)

    # Inicjalizacja obiektów do stylizacji i wizualizacji
    styler = GraphStyler()

    # Losowy wybór węzłów startowego i końcowego
    start_node = random.choice(list(graph.nodes))
    end_node = random.choice(list(graph.nodes))
    print(f"Start: {start_node}, End: {end_node}")

    # Przechowuje wyniki algorytmów
    results = {}

    # BFS
    print("Running BFS...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    bfs = BFSAlgorithm(graph, None, styler)
    result_b = bfs.execute(start_node, end_node, plot=False)
    results["BFS"] = {"path": result_b[0], "cost": result_b[1], "time": result_b[2]}
    print("BFS completed.")

    # Dijkstra
    print("Running Dijkstra...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    dijkstra = DijkstraAlgorithm(graph, None, styler)
    result_d = dijkstra.execute(start_node, end_node, plot=False)
    results["Dijkstra"] = {"path": result_d[0], "cost": result_d[1], "time": result_d[2]}
    print("Dijkstra completed.")

    # A*
    print("Running A*...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    astar = AStarAlgorithm(graph, None, styler)
    result_a = astar.execute(start_node, end_node, plot=False)
    results["A*"] = {"path": result_a[0], "cost": result_a[1], "time": result_a[2]}
    print("A* completed.")

    # Visualize comparisons
    plot_comparisons(results)


if __name__ == "__main__":
    main()
