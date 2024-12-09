"""File containing algorithms' classes and methods."""

import math
import heapq
from typing import Tuple


class BFSAlgorithm:
    """Performs BFS on a graph and visualizes the process."""

    def __init__(self, graph, visualizer, styler):
        """
        Initializes the BFS algorithm.
        :param graph: The graph on which BFS will operate.
        :param visualizer: The object responsible for graph visualization.
        :param styler: The object responsible for styling nodes and edges.
        """
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def execute(self, start: int, end: int, plot: bool = False):
        """
        Executes BFS from start to end with enhanced debugging.
        :param start: The starting node.
        :param end: The target node.
        :param plot: Whether to capture frames for visualization.
        """
        # Highlight start and end nodes
        self.graph.nodes[start]["size"] = 50
        self.graph.nodes[end]["size"] = 50
        queue = [start]
        step = 0

        print(f"Starting BFS from {start} to {end}.")
        while queue:
            current_node = queue.pop(0)

            if current_node == end:
                print(f"End node {end} reached.")
                self.graph.nodes[end][
                    "visited"
                ] = True  # Explicitly mark the end node as visited
                if plot:
                    self.visualizer.capture_frame()
                return

            # Process the current node if it's not visited
            if not self.graph.nodes[current_node]["visited"]:
                print(f"Visiting node: {current_node}")
                self.graph.nodes[current_node]["visited"] = True
                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, queue)

                # Capture frames for visualization
                if plot and step % 10 == 0:
                    self.visualizer.capture_frame()
                step += 1

        # Debugging output if BFS fails to reach the end node
        if not self.graph.nodes[end]["visited"]:
            print(f"BFS failed to reach the end node {end}.")
            visited_nodes = [
                node for node in self.graph.nodes if self.graph.nodes[node]["visited"]
            ]
            print(f"Visited nodes: {visited_nodes}")
            print(f"Total visited nodes: {len(visited_nodes)}")

    def _process_edge(self, edge: Tuple[int, int, int], queue: list):
        """
        Processes an edge during BFS traversal.
        :param edge: A tuple representing the edge (source, target, key).
        :param queue: The BFS queue to which unvisited neighbors are added.
        """
        # Style the edge being processed
        self.styler.style_edge(self.graph, edge, color="#3F50E7", alpha=1, linewidth=1)

        # Get the neighbor node
        neighbor = edge[1]
        if not self.graph.nodes[neighbor]["visited"]:
            print(f"Queueing neighbor: {neighbor} from edge {edge}")
            self.graph.nodes[neighbor]["previous"] = edge[
                0
            ]  # Set the 'previous' node for path reconstruction
            queue.append(neighbor)


class DijkstraAlgorithm:
    """Performs Dijkstra's algorithm on a graph and visualizes the process."""

    def __init__(self, graph, visualizer, styler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def execute(self, start: int, end: int, plot: bool = False):
        """Executes Dijkstra's algorithm from start to end."""
        self.graph.nodes[start]["distance"] = 0
        pq = [(0, start)]
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

    def _process_edge(
        self, edge: Tuple[int, int, int], current_distance: float, pq: list
    ):
        """Processes an edge during Dijkstra's traversal."""
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        new_distance = current_distance + weight

        if new_distance < self.graph.nodes[neighbor]["distance"]:
            self.graph.nodes[neighbor]["distance"] = new_distance
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(pq, (new_distance, neighbor))


class AStarAlgorithm:
    """Performs A* algorithm on a graph and visualizes the process."""

    def __init__(self, graph, visualizer, styler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def execute(self, start: int, end: int, plot: bool = False):
        """Executes A* algorithm from start to end."""
        self.graph.nodes[start]["g_score"] = 0
        self.graph.nodes[start]["f_score"] = self._heuristic(start, end)
        pq = [(0, start)]
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
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        g_score = self.graph.nodes[edge[0]]["g_score"] + weight

        if g_score < self.graph.nodes[neighbor]["g_score"]:
            self.graph.nodes[neighbor]["g_score"] = g_score
            self.graph.nodes[neighbor]["f_score"] = g_score + self._heuristic(
                neighbor, end
            )
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(pq, (self.graph.nodes[neighbor]["f_score"], neighbor))

    def _heuristic(self, node1: int, node2: int) -> float:
        """Calculates the heuristic for A* (Euclidean distance)."""
        x1, y1 = self.graph.nodes[node1]["x"], self.graph.nodes[node1]["y"]
        x2, y2 = self.graph.nodes[node2]["x"], self.graph.nodes[node2]["y"]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


class PathReconstructor:
    """Reconstructs the path found by an algorithm and visualizes it."""

    def __init__(self, graph, visualizer, styler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    def reconstruct_path(self, start: int, end: int, plot: bool = False):
        """Reconstructs the path from end to start."""
        current_node = end

        while current_node != start:
            previous_node = self.graph.nodes[current_node]["previous"]
            if previous_node is None:
                print("Path reconstruction failed: No path found.")
                return
            edge = (previous_node, current_node, 0)
            self.styler.style_edge(
                self.graph, edge, color="white", alpha=1, linewidth=1
            )
            current_node = previous_node

        if plot:
            for _ in range(60):
                self.visualizer.capture_frame()
