from core import GraphAlgorithm
from core.decorators import log_execution, measure_time
from typing import Tuple, AsyncGenerator
import heapq
import math


class AStarAlgorithm(GraphAlgorithm):
    """
    Implements the A* algorithm for pathfinding using asynchronous generators for efficient iteration.

    This algorithm operates on a graph and finds the shortest path from a start node to an end node.
    It uses a heuristic function (Euclidean distance) to guide the search.

    Integration:
    - Relies on the `GraphVisualizer` for capturing the state during execution.
    - Uses the `GraphStyler` to style nodes and edges for visualization.
    """

    """
    Implements the A* algorithm for pathfinding using asynchronous generators for efficient iteration.

    This algorithm operates on a graph and finds the shortest path from a start node to an end node.
    It uses a heuristic function (Euclidean distance) to guide the search.
    """

    @log_execution
    @measure_time
    async def execute(self, start: int, end: int, plot: bool = False):
        """
        Executes the A* algorithm to find the shortest path from a start node to an end node.

        Args:
            start (int): The starting node of the path.
            end (int): The target node of the path.
            plot (bool, optional): Flag indicating whether to plot the algorithm's progress. Defaults to False.

        Returns:
            None

        Notes:
            - If the path cannot be found, the method exits without an error but does not modify the graph.
            - Logs execution steps for debugging and performance monitoring.
        """
        """
        Executes the A* algorithm to find the shortest path from a start node to an end node.

        Args:
            start (int): The starting node of the path.
            end (int): The target node of the path.
            plot (bool, optional): Flag indicating whether to plot the algorithm's progress. Defaults to False.

        Returns:
            None
        """
        self.initialize_graph()
        self.styler.style_node(self.graph, start, size=50)
        self.styler.style_node(self.graph, end, size=50)

        priority_queue = [(0, start)]  #: (f_score, node)
        self.graph.nodes[start]["g_score"] = 0
        self.graph.nodes[start]["f_score"] = self._heuristic(start, end)

        async for current_node in self._node_iterator(priority_queue, end, plot):
            if current_node == end:
                return

    async def _node_iterator(
        self, priority_queue: list, end: int, plot: bool
    ) -> AsyncGenerator[int, None]:
        """
        Asynchronous generator that iterates over nodes in a priority queue.

        Args:
            priority_queue (list): The priority queue used to determine the next node to visit.
            end (int): The target node for the algorithm.
            plot (bool): Flag indicating whether to capture frames for visualization. Defaults to False.

        Yields:
            int: The current node being processed.
        """
        step = 0
        while priority_queue:
            _, current_node = heapq.heappop(priority_queue)

            if not self.graph.nodes[current_node]["visited"]:
                self.graph.nodes[current_node]["visited"] = True

                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, end, priority_queue)

                if plot and step % 10 == 0:
                    await self.visualizer.capture_frame()
                step += 1

            yield current_node

    def _process_edge(self, edge: Tuple[int, int, int], end: int, priority_queue: list):
        """
        Processes an edge during the A* algorithm's execution.

        Updates the g_score and f_score for the neighbor node if a shorter path is found.

        Args:
            edge (Tuple[int, int, int]): A tuple representing the edge (start_node, neighbor_node, edge_id).
            end (int): The target node for the algorithm.
            priority_queue (list): The priority queue used to schedule nodes for processing.

        Returns:
            None

        Edge Cases:
            - If the edge lacks a valid weight, default values should be handled gracefully.
            - Assumes the graph's edges have been preprocessed with weights.
        """
        """
        Processes an edge during the A* algorithm's execution.

        Updates the g_score and f_score for the neighbor node if a shorter path is found.

        Args:
            edge (Tuple[int, int, int]): A tuple representing the edge (start_node, neighbor_node, edge_id).
            end (int): The target node for the algorithm.
            priority_queue (list): The priority queue used to schedule nodes for processing.

        Returns:
            None
        """
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        g_score = self.graph.nodes[edge[0]]["g_score"] + weight

        if g_score < self.graph.nodes[neighbor]["g_score"]:
            self.graph.nodes[neighbor]["g_score"] = g_score
            self.graph.nodes[neighbor]["f_score"] = g_score + self._heuristic(
                neighbor, end
            )
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(
                priority_queue, (self.graph.nodes[neighbor]["f_score"], neighbor)
            )

        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=3)

    def _heuristic(self, node1: int, node2: int) -> float:
        """
        Calculates the heuristic value (Euclidean distance) between two nodes.

        Args:
            node1 (int): The first node's identifier.
            node2 (int): The second node's identifier.

        Returns:
            float: The Euclidean distance between the two nodes.
        """
        x1, y1 = self.graph.nodes[node1]["x"], self.graph.nodes[node1]["y"]
        x2, y2 = self.graph.nodes[node2]["x"], self.graph.nodes[node2]["y"]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
