from core import GraphAlgorithm
from core.decorators import log_execution, measure_time
from typing import Tuple, AsyncGenerator


class BFSAlgorithm(GraphAlgorithm):
    """
    Breadth-First Search (BFS) Algorithm implementation.

    This class provides an implementation of the BFS algorithm
    using generators for efficient traversal. It extends the
    `GraphAlgorithm` base class and provides methods for executing
    BFS on a graph structure with optional visualization support.

    Attributes:
        graph: The graph structure to traverse.
        styler: A utility for styling nodes and edges in the graph.
        visualizer: A utility for capturing and visualizing traversal frames.
    """

    @log_execution
    @measure_time
    async def execute(self, start: int, end: int, plot: bool = False):
        """
        Executes the BFS algorithm to traverse a graph from a start node to an end node.

        Args:
            start (int): The starting node for the BFS traversal.
            end (int): The target node to reach during the traversal.
            plot (bool, optional): Whether to visualize the traversal process. Defaults to False.

        Returns:
            None: This method performs traversal and does not return a value.

        Raises:
            Exception: Any exceptions raised during graph initialization or traversal.
        """
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
        """
        Asynchronous generator that iterates over nodes in the BFS queue.

        Args:
            queue (list): The queue containing nodes to be processed.
            plot (bool): Whether to visualize each step of the traversal.

        Yields:
            int: The current node being processed.

        Raises:
            Exception: Any exceptions encountered during node iteration.
        """
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
        """
        Processes an edge during the BFS traversal.

        This method styles the edge and adds the neighbor node to the queue if it has not been visited.

        Args:
            edge (Tuple[int, int, int]): The edge to process, represented as a tuple (source, target, key).
            queue (list): The queue to which unvisited neighbor nodes will be added.

        Returns:
            None: This method modifies the graph and queue in place.

        Raises:
            Exception: Any exceptions related to graph node or edge processing.
        """
        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=3)
        neighbor = edge[1]
        if not self.graph.nodes[neighbor]["visited"]:
            self.graph.nodes[neighbor]["previous"] = edge[0]
            queue.append(neighbor)
