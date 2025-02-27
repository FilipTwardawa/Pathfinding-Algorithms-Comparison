"""
Algorithm Comparator Module

This module provides a framework for comparing the performance of different pathfinding algorithms
on a given graph. It includes methods for initializing algorithms, running comparisons,
collecting metrics, and generating visualizations.

Classes:
    AlgorithmComparator: Facilitates the comparison of pathfinding algorithms' performance.
"""

import asyncio
import os
import time
import pandas as pd
import matplotlib.pyplot as plt
from utils import initialize_graph
from core import GraphStyler, GraphProcessor
import importlib

# Metrics
TIME_METRIC = "Time (s)"
COST_METRIC = "Total Cost"
STEPS_METRIC = "Steps"
PATH_LENGTH_METRIC = "Path Length"


class AlgorithmComparator:
    """
    A class to compare the performance of multiple pathfinding algorithms.

    Attributes:
        graph (Graph): The graph instance on which the algorithms will run.
        start_node (Any): The starting node for the algorithms.
        end_node (Any): The target node for the algorithms.
        algorithms (dict): A dictionary of algorithms to compare.
        results (list): A list to store the performance results of the algorithms.
    """

    def __init__(self, graph, start_node, end_node):
        """
        Initializes the AlgorithmComparator with the provided graph and nodes.

        Args:
            graph (Graph): The graph instance on which the algorithms will run.
            start_node (Any): The starting node for the algorithms.
            end_node (Any): The target node for the algorithms.
        """
        dijkstra_algorithm = getattr(importlib.import_module("algorithms.dijkstra"), "DijkstraAlgorithm")
        a_star_algorithm = getattr(importlib.import_module("algorithms.a_star"), "AStarAlgorithm")
        bfs_algorithm = getattr(importlib.import_module("algorithms.bfs"), "BFSAlgorithm")

        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node
        self.algorithms = {
            "Dijkstra": dijkstra_algorithm(graph, None, GraphStyler()),
            "A*": a_star_algorithm(graph, None, GraphStyler()),
            "BFS": bfs_algorithm(graph, None, GraphStyler()),
        }
        self.results = []

    def run_comparison(self, plot=False):
        """
        Runs all algorithms and records their performance metrics.

        Args:
            plot (bool): Whether to visualize the algorithms' execution on the graph. Defaults to False.
        """
        for name, algorithm in self.algorithms.items():
            print(f"Running {name}...")
            GraphProcessor.initialize_nodes(self.graph)
            GraphProcessor.initialize_edges(self.graph, GraphStyler())

            start_time = time.time()
            try:
                asyncio.run(algorithm.execute(self.start_node, self.end_node, plot))
                duration = time.time() - start_time
                cost, steps, path_length = self._collect_metrics()
                if cost == 0 and path_length == 0:
                    print(f"{name} failed to find a valid path.")
                    continue
                self.results.append({
                    "Algorithm": name,
                    TIME_METRIC: duration,
                    COST_METRIC: cost,
                    STEPS_METRIC: steps,
                    PATH_LENGTH_METRIC: path_length,
                })
                print(
                    f"{name} completed in {duration:.4f}s with cost={cost}, steps={steps}, path_length={path_length}.")
            except Exception as e:
                print(f"Error running {name}: {e}")

    def _collect_metrics(self):
        """
        Collects metrics for an algorithm's execution, including cost, steps, and path length.

        Returns:
            tuple: A tuple containing the total cost, number of steps, and path length.
        """
        cost = 0
        steps = 0
        path_length = 0
        current_node = self.end_node

        while current_node is not None and self.graph.nodes[current_node].get("previous") is not None:
            prev_node = self.graph.nodes[current_node]["previous"]
            edge_data = self.graph.get_edge_data(prev_node, current_node, default={})
            edge_weight = edge_data.get("weight", 0)

            if edge_weight == 0:
                print(f"⚠️ Missing weight for edge ({prev_node}, {current_node}). Defaulting to 1.")
                edge_weight = 1

            cost += edge_weight
            steps += 1
            path_length += 1
            current_node = prev_node

        return cost, steps, path_length

    def generate_visualizations(self, output_dir="results/comparisons"):
        """
        Generates and saves comparison charts for the algorithm performance metrics.

        Args:
            output_dir (str): The directory where the visualizations will be saved. Defaults to "results/comparisons".
        """
        if not self.results:
            print("No valid results to visualize.")
            return

        os.makedirs(output_dir, exist_ok=True)
        df = pd.DataFrame(self.results)

        metrics = [TIME_METRIC, COST_METRIC, STEPS_METRIC, PATH_LENGTH_METRIC]
        for metric in metrics:
            plt.figure(figsize=(10, 6))
            plt.bar(df["Algorithm"], df[metric], color=["#4CAF50", "#FF9800", "#2196F3"])
            plt.title(f"Algorithm Comparison: {metric}")
            plt.ylabel(metric)
            plt.xlabel("Algorithms")
            output_path = os.path.join(output_dir, f"algorithm_comparison_{metric.lower().replace(' ', '_')}.png")
            plt.savefig(output_path)
            plt.close()
            print(f"Saved {metric} comparison chart: {output_path}")


if __name__ == "__main__":
    """
    Main execution flow for the AlgorithmComparator.
    Initializes the graph and runs comparisons and visualizations.
    """
    graph_instance = initialize_graph("Gliwice, Poland")
    start_node_instance = list(graph_instance.nodes)[0]
    end_node_instance = list(graph_instance.nodes)[-1]

    comparator = AlgorithmComparator(graph_instance, start_node_instance, end_node_instance)
    comparator.run_comparison(plot=False)
    comparator.generate_visualizations()

    if comparator.results:
        print("\nSummary of Algorithm Performance:")
        for result in comparator.results:
            print(f"Algorithm: {result['Algorithm']}")
            print(f"  - Time (s): {result[TIME_METRIC]:.4f}")
            print(f"  - Total Cost: {result[COST_METRIC]:.4f}")
            print(f"  - Steps: {result[STEPS_METRIC]}")
            print(f"  - Path Length: {result[PATH_LENGTH_METRIC]}\n")
    else:
        print("No valid results to summarize.")
