from core import GraphAlgorithm
from core.decorators import log_execution, measure_time
from typing import Tuple, AsyncGenerator
import heapq
import math


class AStarAlgorithm(GraphAlgorithm):
    """Performs A* algorithm using generators for efficient iteration."""

    @log_execution
    @measure_time
    async def execute(self, start: int, end: int, plot: bool = False):
        """Performs the A* algorithm using generators."""
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
        """A generator that iterates over vertices in a priority queue."""
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
        """Przetwarza krawędź podczas iteracji."""
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        g_score = self.graph.nodes[edge[0]]["g_score"] + weight

        if g_score < self.graph.nodes[neighbor]["g_score"]:
            self.graph.nodes[neighbor]["g_score"] = g_score
            self.graph.nodes[neighbor]["f_score"] = g_score + self._heuristic(neighbor, end)
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(priority_queue, (self.graph.nodes[neighbor]["f_score"], neighbor))

        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=3)

    def _heuristic(self, node1: int, node2: int) -> float:
        """Calculates heuristics (Euclidean distance)."""
        x1, y1 = self.graph.nodes[node1]["x"], self.graph.nodes[node1]["y"]
        x2, y2 = self.graph.nodes[node2]["x"], self.graph.nodes[node2]["y"]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
