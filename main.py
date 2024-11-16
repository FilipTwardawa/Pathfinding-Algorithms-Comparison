import random
from io import BytesIO
from typing import Tuple
import matplotlib.pyplot as plt
import osmnx as ox
from PIL import Image
import math
import heapq


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


class BFSAlgorithm:
    """Performs BFS on a graph and visualizes the process."""

    def __init__(self, graph, visualizer: GraphVisualizer, styler: GraphStyler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def execute(self, start: int, end: int, plot: bool = False):
        """Executes BFS from start to end."""
        GraphProcessor.initialize_nodes(self.graph)
        self.styler.style_node(self.graph, start, size=50)
        self.styler.style_node(self.graph, end, size=50)
        queue = [start]
        step = 0

        while queue:
            current_node = queue.pop(0)

            if current_node == end:
                if plot:
                    self.visualizer.capture_frame()
                return

            if not self.graph.nodes[current_node]["visited"]:
                self.graph.nodes[current_node]["visited"] = True
                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, queue)

                if plot and step % 10 == 0:
                    self.visualizer.capture_frame()
                step += 1

    def _process_edge(self, edge: Tuple[int, int, int], queue: list):
        """Processes an edge during BFS traversal."""
        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=1)
        neighbor = edge[1]
        if not self.graph.nodes[neighbor]["visited"]:
            self.graph.nodes[neighbor]["previous"] = edge[0]
            queue.append(neighbor)
            self.styler.style_edge(self.graph, edge, color="#3F50E7", alpha=1, linewidth=1)


class DijkstraAlgorithm:
    """Performs Dijkstra's algorithm on a graph and visualizes the process."""

    def __init__(self, graph, visualizer: GraphVisualizer, styler: GraphStyler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def execute(self, start: int, end: int, plot: bool = False):
        """Executes Dijkstra's algorithm from start to end."""
        GraphProcessor.initialize_nodes(self.graph)
        self.styler.style_node(self.graph, start, size=50)
        self.styler.style_node(self.graph, end, size=50)

        pq = [(0, start)]  # Priority queue
        self.graph.nodes[start]["distance"] = 0
        step = 0

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == end:

                return

            if not self.graph.nodes[current_node]["visited"]:
                self.graph.nodes[current_node]["visited"] = True
                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, current_distance, pq)


                if plot and step % 10 == 0:
                    self.visualizer.capture_frame()
                step += 1

    def _process_edge(self, edge: Tuple[int, int, int], current_distance: float, pq: list):
        """Processes an edge during Dijkstra's traversal."""
        self.styler.style_edge(self.graph, edge, color="#3F50E7", alpha=1, linewidth=1)
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        new_distance = current_distance + weight

        if new_distance < self.graph.nodes[neighbor]["distance"]:
            self.graph.nodes[neighbor]["distance"] = new_distance
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(pq, (new_distance, neighbor))


class AStarAlgorithm:
    """Performs A* algorithm on a graph and visualizes the process."""

    def __init__(self, graph, visualizer: GraphVisualizer, styler: GraphStyler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def execute(self, start: int, end: int, plot: bool = False):
        """Executes A* algorithm from start to end."""
        GraphProcessor.initialize_nodes(self.graph)
        self.styler.style_node(self.graph, start, size=50)
        self.styler.style_node(self.graph, end, size=50)

        pq = [(0, start)]  # Priority queue
        self.graph.nodes[start]["g_score"] = 0
        self.graph.nodes[start]["f_score"] = self._heuristic(start, end)
        step = 0

        while pq:
            _, current_node = heapq.heappop(pq)

            if current_node == end:

                return

            if not self.graph.nodes[current_node]["visited"]:
                self.graph.nodes[current_node]["visited"] = True
                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, end, pq)


                if plot and step % 10 == 0:
                    self.visualizer.capture_frame()
                step += 1

    def _process_edge(self, edge: Tuple[int, int, int], end: int, pq: list):
        """Processes an edge during A* traversal."""
        self.styler.style_edge(self.graph, edge, color="#3F50E7", alpha=1, linewidth=1)
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        g_score = self.graph.nodes[edge[0]]["g_score"] + weight

        if g_score < self.graph.nodes[neighbor]["g_score"]:
            self.graph.nodes[neighbor]["g_score"] = g_score
            self.graph.nodes[neighbor]["f_score"] = g_score + self._heuristic(neighbor, end)
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(pq, (self.graph.nodes[neighbor]["f_score"], neighbor))

    def _heuristic(self, node1: int, node2: int) -> float:
        """Calculates the heuristic for A* (Euclidean distance)."""
        x1, y1 = self.graph.nodes[node1]["x"], self.graph.nodes[node1]["y"]
        x2, y2 = self.graph.nodes[node2]["x"], self.graph.nodes[node2]["y"]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

class PathReconstructor:
    """Reconstructs the path found by an algorithm and visualizes it."""

    def __init__(self, graph, visualizer: GraphVisualizer, styler: GraphStyler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def reconstruct_path(self, start: int, end: int, plot: bool = False):
        """Reconstructs the path from end to start."""
        # Reset edges to remove any previous styling
        GraphProcessor.initialize_edges(self.graph, self.styler)

        current_node = end
        step_count = 0

        while current_node != start:
            previous_node = self.graph.nodes[current_node]["previous"]
            if previous_node is None:
                print("Path reconstruction failed: No path found.")
                return
            edge = (previous_node, current_node, 0)
            self.styler.style_edge(self.graph, edge, color="white", alpha=1, linewidth=1)
            current_node = previous_node
            step_count += 1

            if plot and step_count % 2 == 0:
                self.visualizer.capture_frame()

        if plot:
            self._add_final_frames()

    def _add_final_frames(self):
        """Adds extra frames for smooth GIF ending."""
        for _ in range(60):
            self.visualizer.capture_frame()



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


def main():
    place_name = "Gliwice, Poland"
    graph = initialize_graph(place_name)

    styler = GraphStyler()

    start = random.choice(list(graph.nodes))
    end = random.choice(list(graph.nodes))

    # Run BFS
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    bfs_visualizer = GraphVisualizer(graph)
    bfs = BFSAlgorithm(graph, bfs_visualizer, styler)
    bfs.execute(start, end, plot=True)

    # Reconstruct path for BFS
    reconstructor = PathReconstructor(graph, bfs_visualizer, styler)
    reconstructor.reconstruct_path(start, end, plot=True)

    # Save GIF for BFS
    bfs_visualizer.save_gif("bfs_animation.gif")

    # Run Dijkstra
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    dijkstra_visualizer = GraphVisualizer(graph)
    dijkstra = DijkstraAlgorithm(graph, dijkstra_visualizer, styler)
    dijkstra.execute(start, end, plot=True)

    # Reconstruct path for Dijkstra
    reconstructor = PathReconstructor(graph, dijkstra_visualizer, styler)
    reconstructor.reconstruct_path(start, end, plot=True)

    # Save GIF for Dijkstra
    dijkstra_visualizer.save_gif("dijkstra_animation.gif")

    # Run A*
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    astar_visualizer = GraphVisualizer(graph)
    astar = AStarAlgorithm(graph, astar_visualizer, styler)
    astar.execute(start, end, plot=True)

    # Reconstruct path for A*
    reconstructor = PathReconstructor(graph, astar_visualizer, styler)
    reconstructor.reconstruct_path(start, end, plot=True)

    # Save GIF for A*
    astar_visualizer.save_gif("astar_animation.gif")


if __name__ == "__main__":
    main()

