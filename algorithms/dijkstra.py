from core import GraphAlgorithm
from core.decorators import log_execution, measure_time
from typing import Tuple, AsyncGenerator
import heapq


class DijkstraAlgorithm(GraphAlgorithm):
    """
    Implements Dijkstra's shortest path algorithm using asynchronous generators
    for efficient graph traversal.

    This algorithm calculates the shortest path between a start node and an
    end node in a weighted graph, leveraging priority queues for optimal
    performance. The implementation supports real-time visualization and
    node/edge styling.
    """

    @log_execution
    @measure_time
    async def execute(self, start: int, end: int, plot: bool = False):
        """
        Executes Dijkstra's algorithm to compute the shortest path in the graph.

        Args:
            start (int): The starting node for the algorithm.
            end (int): The target node for the algorithm.
            plot (bool, optional): Whether to visualize the graph traversal.
                Defaults to False.

        Returns:
            None
        """
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
        """
        Asynchronous generator for traversing nodes in the priority queue.

        Args:
            priority_queue (list): A list of tuples representing the nodes
                to process, with their associated distances.
            plot (bool): Whether to capture frames during traversal for visualization.

        Yields:
            int: The current node being processed.
        """
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
        """
        Processes an edge during the traversal of the graph in Dijkstra's algorithm.

        Updates the distance to neighboring nodes and manages the priority queue.

        Args:
            edge (Tuple[int, int, int]): A tuple representing the edge in the graph,
                containing the source node, target node, and edge key.
            current_distance (float): The distance from the start node to the
                current node.
            priority_queue (list): The priority queue used for managing nodes
                to visit next.

        Returns:
            None
        """
        neighbor = edge[1]
        weight = self.graph.edges[edge]["weight"]
        new_distance = current_distance + weight

        if new_distance < self.graph.nodes[neighbor]["distance"]:
            self.graph.nodes[neighbor]["distance"] = new_distance
            self.graph.nodes[neighbor]["previous"] = edge[0]
            heapq.heappush(priority_queue, (new_distance, neighbor))

        self.styler.style_edge(self.graph, edge, color="#2432B0", alpha=1, linewidth=3)
