from core import GraphProcessor, GraphVisualizer, GraphStyler
import logging

logger = logging.getLogger(__name__)


class PathReconstructor:
    """Reconstructs the path found by an algorithm and visualizes it asynchronously."""

    def __init__(self, graph, visualizer: GraphVisualizer, styler: GraphStyler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    async def reconstruct_path(self, start: int, end: int, plot: bool = False):
        """Replays the path from endpoint to start asynchronously with error handling."""
        try:
            GraphProcessor.initialize_edges(self.graph, self.styler)
            async for edge in self._path_generator(start, end):
                try:
                    self.styler.style_edge(self.graph, edge, color="#ADD8E6", alpha=0.9, linewidth=2)
                    if plot:
                        await self.visualizer.capture_frame()
                except Exception as e:
                    logger.error(f"Error styling or capturing frame for edge {edge}: {e}")
                    continue
            if plot:
                await self._add_final_frames()
        except Exception as e:
            logger.error(f"Error reconstructing path: {e}")

    async def _path_generator(self, start: int, end: int):
        """Asynchronous generator that plays the track from the end to the beginning."""
        current_node = end
        while current_node != start:
            previous_node = self.graph.nodes[current_node].get("previous")
            if previous_node is None:
                logger.error("Path reconstruction failed: No path found.")
                return
            yield previous_node, current_node, 0  # (source, target, key)
            current_node = previous_node

    async def _add_final_frames(self):
        """Adds extra frames for smoother GIF visualization."""
        try:
            for _ in range(60):
                await self.visualizer.capture_frame()
        except Exception as e:
            logger.error(f"Error adding final frames: {e}")
