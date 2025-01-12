from core import GraphAlgorithm
from core.decorators import log_execution, measure_time
from typing import Tuple, AsyncGenerator
import heapq


class DijkstraAlgorithm(GraphAlgorithm):
    """Performs Dijkstra's algorithm using generators for efficient traversal."""

    @log_execution
    @measure_time
    async def execute(self, start: int, end: int, plot: bool = False):
        """Performs the Dijkstra algorithm using generators."""
        self.initialize_graph()
        self.styler.style_node(self.graph, start, size=50)
        self.styler.style_node(self.graph, end, size=50)

        priority_queue = [(0, start)]  # : (distance, node)
        self.graph.nodes[start]["distance"] = 0

        async for current_node in self._node_iterator(priority_queue, plot):
            if current_node == end:
                return

    async def _node_iterator(
        self, priority_queue: list, plot: bool
    ) -> AsyncGenerator[int, None]:
        """A generator that iterates over vertices in a priority queue."""
        step = 0
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if not self.graph.nodes[current_node]["visited"]:
                self.graph.nodes[current_node]["visited"] = True

                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, current_distance, priority_queue)

                if plot and step % 10 == 0:
                    await self.visualizer.capture_frame()
                step += 1

            yield current_node

    def _process_edge(
        self, edge: Tuple[int, int, int], current_distance: float, priority_queue: list
    ):
        """Processes the edge during the iteration of the Dijkstra algorithm."""
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        new_distance = current_distance + weight

        if new_distance < self.graph.nodes[neighbor]["distance"]:
            self.graph.nodes[neighbor]["distance"] = new_distance
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(priority_queue, (new_distance, neighbor))

        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=3)