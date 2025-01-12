from core import GraphAlgorithm
from core.decorators import log_execution, measure_time
from typing import Tuple, AsyncGenerator


class BFSAlgorithm(GraphAlgorithm):
    """Performs BFS using generators for efficient traversal."""

    @log_execution
    @measure_time
    async def execute(self, start: int, end: int, plot: bool = False):
        """Performs the BFS algorithm using generators."""
        self.initialize_graph()
        self.styler.style_node(self.graph, start, size=50)
        self.styler.style_node(self.graph, end, size=50)

        queue = [start]
        async for current_node in self._node_iterator(queue, plot):
            if current_node == end:
                return

    async def _node_iterator(
        self, queue: list, plot: bool
    ) -> AsyncGenerator[int, None]:
        """A generator that iterates over vertices in a BFS queue."""
        step = 0
        while queue:
            current_node = queue.pop(0)

            if not self.graph.nodes[current_node]["visited"]:
                self.graph.nodes[current_node]["visited"] = True

                for edge in self.graph.out_edges(current_node, keys=True):
                    self._process_edge(edge, queue)

                if plot and step % 10 == 0:
                    await self.visualizer.capture_frame()
                step += 1

            yield current_node

    def _process_edge(self, edge: Tuple[int, int, int], queue: list):
        """Processes the edge during BFS."""
        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=3)
        neighbor = edge[1]
        if not self.graph.nodes[neighbor]["visited"]:
            self.graph.nodes[neighbor]["previous"] = edge[0]
            queue.append(neighbor)