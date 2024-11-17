import osmnx as ox
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt


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


class GraphVisualizer:
    """Manages visualization and GIF creation for a graph."""

    def __init__(self, graph):
        self.graph = graph
        self.frames = []  # Stores frames for GIF generation

    def capture_frame(self):
        """Captures the current state of the graph as an image frame."""
        fig, ax = ox.plot_graph(
            self.graph,
            node_size=[self.graph.nodes[node].get("size", 0) for node in self.graph.nodes],
            edge_color=[self.graph.edges[edge].get("color", "#2432B0") for edge in self.graph.edges],
            edge_alpha=[self.graph.edges[edge].get("alpha", 0.3) for edge in self.graph.edges],
            edge_linewidth=[self.graph.edges[edge].get("linewidth", 0.5) for edge in self.graph.edges],
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
        """Generates a GIF from the captured frames."""
        if self.frames:
            self.frames[0].save(
                gif_filename,
                save_all=True,
                append_images=self.frames[1:],
                duration=duration,
                loop=0
            )
            print(f"GIF saved as {gif_filename}")


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
        for edge in graph.edges:
            styler.style_edge(graph, edge)


def initialize_graph(place_name: str):
    """Initializes the graph and sets edge weights."""
    graph = ox.graph_from_place(place_name, network_type='drive')
    for edge in graph.edges:
        maxspeed = 40
        if "maxspeed" in graph.edges[edge]:
            maxspeed_value = graph.edges[edge]["maxspeed"]
            maxspeed = int(maxspeed_value) if isinstance(maxspeed_value, str) and maxspeed_value.isdigit() else maxspeed
        graph.edges[edge].update({"maxspeed": maxspeed, "weight": graph.edges[edge]["length"] / maxspeed})
    return graph
