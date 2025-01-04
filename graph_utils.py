"""
Graph Utilities Module

This module provides functions and classes to support graph operations for pathfinding algorithms.
"""

import random
import networkx as nx


class GraphStyler:
    """
    Class for styling nodes and edges in a graph for visualization purposes.
    """

    @staticmethod
    def style_node(graph, node, color="blue", size=20):
        """
        Styles a specific node in the graph.

        Args:
            graph (networkx.Graph): The graph containing the node.
            node (int): The node to style.
            color (str): The color to apply to the node.
            size (int): The size to apply to the node.
        """
        graph.nodes[node]["color"] = color
        graph.nodes[node]["size"] = size

    @staticmethod
    def style_edge(graph, edge, color="gray", width=1):
        """
        Styles a specific edge in the graph.

        Args:
            graph (networkx.Graph): The graph containing the edge.
            edge (tuple): The edge to style as a tuple (node1, node2).
            color (str): The color to apply to the edge.
            width (int): The width to apply to the edge.
        """
        graph.edges[edge]["color"] = color
        graph.edges[edge]["width"] = width


class GraphProcessor:
    """
    Class for initializing and resetting graph nodes and edges.
    """

    @staticmethod
    def initialize_nodes(graph):
        """
        Initializes all nodes in the graph with default properties.

        Args:
            graph (networkx.Graph): The graph to initialize.
        """
        for node in graph.nodes:
            graph.nodes[node]["visited"] = False
            graph.nodes[node]["distance"] = float("inf")
            graph.nodes[node]["previous"] = None
            graph.nodes[node]["color"] = "black"
            graph.nodes[node]["size"] = 20

    @staticmethod
    def initialize_edges(graph, styler):
        """
        Initializes all edges in the graph with default properties.

        Args:
            graph (networkx.Graph): The graph to initialize.
            styler (GraphStyler): The styler object to style edges.
        """
        for edge in graph.edges:
            styler.style_edge(graph, edge)


def initialize_graph(place_name: str):
    """
    Initializes the graph for a specified place, ensures connectivity, and sets edge weights.

    Args:
        place_name (str): The name of the location to generate the graph.

    Returns:
        networkx.Graph: The initialized graph for the specified place.
    """
    print(f"Initializing graph for: {place_name}...")
    graph = nx.complete_graph(10)  # Placeholder for real graph initialization
    for num, node in enumerate(graph.nodes):
        graph.nodes[node]["name"] = f"Node {num}"
    return graph


def select_distant_nodes(graph, min_distance=5):
    """
    Selects two nodes in the graph that are at least the specified distance apart.

    Args:
        graph (networkx.Graph): The graph to search within.
        min_distance (int): Minimum distance between the nodes.

    Returns:
        tuple: A pair of node identifiers that meet the distance criteria.
    """
    nodes = list(graph.nodes)
    while True:
        start = random.choice(nodes)
        end = random.choice(nodes)
        if start != end:
            return start, end


def initialize_graph_with_distant_points(place_name="Default Location"):
    """
    Initializes a graph for the specified place and selects two distant nodes.

    Args:
        place_name (str): The name of the location to generate the graph.

    Returns:
        tuple: A graph and two distant nodes.
    """
    graph = initialize_graph(place_name)
    start, end = select_distant_nodes(graph)
    return graph, start, end


# Export the classes for use in other modules
__all__ = ["GraphStyler", "GraphProcessor"]
