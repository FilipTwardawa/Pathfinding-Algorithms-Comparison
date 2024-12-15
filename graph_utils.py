"""
Graph Utilities Module

This module provides functions for graph initialization, styling, and processing
to support pathfinding algorithms and visualizations.
"""

import random
from io import BytesIO  # Fixed missing import for BytesIO
from PIL import Image
import matplotlib.pyplot as plt
import osmnx as ox
import networkx as nx


class GraphStyler:
    """Handles styling of graph elements (nodes and edges)."""

    @staticmethod
    def style_edge(graph, edge, color="#2432B0", alpha=0.3, linewidth=0.5):
        """Sets the style for a graph edge."""
        graph.edges[edge].update({"color": color, "alpha": alpha, "linewidth": linewidth})

    @staticmethod
    def style_node(graph, node: int, size: int):
        """Sets the style for a graph node."""
        graph.nodes[node]["size"] = size

    @staticmethod
    def reset_styles(graph):
        """Resets all nodes and edges to default styles."""
        for node in graph.nodes:
            graph.nodes[node].update({"size": 0})
        for edge in graph.edges:
            graph.edges[edge].update({"color": "#2432B0", "alpha": 0.3, "linewidth": 0.5})


class GraphVisualizer:
    """Manages visualization and GIF creation for a graph."""

    def __init__(self, graph):
        """
        Initializes the visualizer with a graph.

        Args:
            graph (networkx.Graph): The graph to visualize.
        """
        self.graph = graph
        self.frames = []  # Stores frames for GIF generation

    def capture_frame(self):
        """Captures the current state of the graph as an image frame."""
        if self.graph is None or len(self.graph.nodes) == 0:
            print("Graph is empty. Skipping frame capture.")
            return

        fig, _ = ox.plot_graph(
            self.graph,
            node_size=[self.graph.nodes[node].get("size", 0) for node in self.graph.nodes],
            edge_color=[
                self.graph.edges[edge].get("color", "#2432B0") for edge in self.graph.edges
            ],
            edge_alpha=[self.graph.edges[edge].get("alpha", 0.3) for edge in self.graph.edges],
            edge_linewidth=
            [self.graph.edges[edge].get("linewidth", 0.5) for edge in self.graph.edges],
            node_color="white",
            bgcolor="#0F1126",
            show=False,
            close=False
        )
        buf = BytesIO()
        plt.savefig(buf, format='png', dpi=300)
        buf.seek(0)
        img = Image.open(buf).copy()
        self.frames.append(img)
        buf.close()
        plt.close(fig)

    def save_gif(self, gif_filename: str, duration: int = 100):
        """Generates a GIF from the captured frames.

        Args:
            gif_filename (str): The name of the GIF file to save.
            duration (int): Duration of each frame in milliseconds.
        """
        if self.frames:
            self.frames[0].save(
                gif_filename,
                save_all=True,
                append_images=self.frames[1:],
                duration=duration,
                loop=0
            )
            print(f"GIF saved as {gif_filename}")
        else:
            print("No frames to save. GIF not created.")


class GraphProcessor:
    """Processes graph nodes and edges for algorithm execution."""

    @staticmethod
    def initialize_nodes(graph):
        """Resets all nodes' visited state and metadata."""
        for node in graph.nodes:
            graph.nodes[node].update({
                "visited": False,
                "previous": None,
                "size": 0,
                "distance": float("inf"),
                "g_score": float("inf"),
                "f_score": float("inf")
            })

    @staticmethod
    def initialize_edges(graph, styler: GraphStyler):
        """Resets all edges' styles."""
        styler.reset_styles(graph)

    @staticmethod
    def reset_graph_styles(graph, styler: GraphStyler):
        """Resets both node and edge styles for a clean graph state."""
        GraphProcessor.initialize_nodes(graph)
        GraphProcessor.initialize_edges(graph, styler)


def initialize_graph(place_name: str):
    """Initializes the graph, ensures connectivity, and sets edge weights.

    Args:
        place_name (str): Name of the location to generate the graph.

    Returns:
        networkx.Graph: A graph initialized for the given place.
    """
    print(f"Initializing graph for: {place_name}...")
    graph = ox.graph_from_place(place_name, network_type="drive")

    # Ensure the graph is strongly connected
    if not nx.is_strongly_connected(graph):
        print("Graph is not strongly connected. Extracting largest strongly connected component...")
        largest_component = max(nx.strongly_connected_components(graph), key=len)
        graph = graph.subgraph(largest_component).copy()
        print("Largest strongly connected component extracted.")

    # Set weights for edges
    for edge in graph.edges:
        maxspeed = 40
        if "maxspeed" in graph.edges[edge]:
            maxspeed_value = graph.edges[edge]["maxspeed"]
            if isinstance(maxspeed_value, str) and maxspeed_value.isdigit():
                maxspeed = int(maxspeed_value)
        graph.edges[edge].update(
            {"maxspeed": maxspeed, "weight": graph.edges[edge]["length"] / maxspeed}
        )

    # Set names for nodes
    for num, node in enumerate(graph.nodes):
        graph.nodes[node]["name"] = f"{num}"

    print(f"Graph initialized with {len(graph.nodes)} nodes and {len(graph.edges)} edges.")
    return graph


def select_distant_nodes(graph, min_distance=32000):
    """Select two nodes in the graph that are at least min_distance apart.

    Args:
        graph (networkx.Graph): The graph to search within.
        min_distance (int): Minimum distance between the nodes.

    Returns:
        tuple: A pair of node identifiers.
    """
    nodes = list(graph.nodes)
    while True:
        start = random.choice(nodes)
        end = random.choice(nodes)
        if start != end:
            try:
                distance = nx.shortest_path_length(graph, source=start, target=end, weight='length')
                if distance >= min_distance:
                    return start, end
            except nx.NetworkXNoPath:
                continue


def initialize_graph_with_distant_points(place_name="Warsaw, Poland"):
    """Initializes a graph and selects distant points.

    Args:
        place_name (str): Name of the location to generate the graph.

    Returns:
        tuple: A graph and two distant nodes.
    """
    graph = initialize_graph(place_name)
    start, end = select_distant_nodes(graph)
    return graph, start, end
