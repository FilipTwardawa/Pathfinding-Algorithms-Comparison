from core import GraphProcessor, GraphVisualizer, GraphStyler
import logging

logger = logging.getLogger(__name__)


class PathReconstructor:
    """Reconstructs the path found by an algorithm and visualizes it asynchronously.

    This class handles the reconstruction of a path in a graph from a start node to an end node.
    It provides functionality to style edges during the reconstruction and optionally generate
    a visualization of the process.
    """

    def __init__(self, graph, visualizer: GraphVisualizer, styler: GraphStyler):
        """Initializes the PathReconstructor.

        Args:
            graph: The graph object containing nodes and edges for pathfinding.
            visualizer (GraphVisualizer): The visualizer instance for generating visual outputs.
            styler (GraphStyler): The styler instance for styling graph edges during reconstruction.
        """
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    async def reconstruct_path(self, start: int, end: int, plot: bool = False):
        """Reconstructs the path from the end node to the start node and optionally plots it.

        Args:
            start (int): The starting node of the path.
            end (int): The ending node of the path.
            plot (bool, optional): Whether to capture and plot frames for visualization. Defaults to False.

        Raises:
            Exception: Logs and handles exceptions during path reconstruction, styling, or visualization.
        """
        try:
            GraphProcessor.initialize_edges(self.graph, self.styler)
            async for edge in self._path_generator(start, end):
                try:
                    self.styler.style_edge(
                        self.graph, edge, color="#ADD8E6", alpha=0.9, linewidth=2
                    )
                    if plot:
                        await self.visualizer.capture_frame()
                except Exception as e:
                    logger.error(
                        f"Error styling or capturing frame for edge {edge}: {e}"
                    )
                    continue
            if plot:
                await self._add_final_frames()
        except Exception as e:
            logger.error(f"Error reconstructing path: {e}")

    async def _path_generator(self, start: int, end: int):
        """
        Generates edges for the path reconstruction asynchronously.

        This method yields edges in the path from the end node to the start node.

        Args:
            start (int): The starting node of the path.
            end (int): The ending node of the path.

        Yields:
            tuple: A tuple containing the source node, target node, and key of an edge.

        Raises:
            RuntimeError: If a path cannot be reconstructed due to missing attributes like `previous`.
            ValueError: If the start or end node is invalid or disconnected.
        """
        current_node = end
        while current_node != start:
            previous_node = self.graph.nodes[current_node].get("previous")
            if previous_node is None:
                logger.error("Path reconstruction failed: No path found.")
                return
            yield previous_node, current_node, 0  # (source, target, key)
            current_node = previous_node

    async def _add_final_frames(self):
        """Adds extra frames to the visualizer for smoother animations.

        This method appends additional frames to the visualization to create a smoother
        transition at the end of the animation.

        Raises:
            Exception: Logs an error if capturing frames fails.
        """
        try:
            for _ in range(60):
                await self.visualizer.capture_frame()
        except Exception as e:
            logger.error(f"Error adding final frames: {e}")
