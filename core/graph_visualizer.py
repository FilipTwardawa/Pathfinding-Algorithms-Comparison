import os
import logging
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import osmnx as ox

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class GraphVisualizer:
    """Manages visualization and GIF creation for a graph.

    This class provides functionality to capture the graphical state of a
    network graph as image frames and compile those frames into an animated GIF.

    Attributes:
        graph: The graph object to visualize, typically a NetworkX graph.
        frames: A list of image frames captured from the graph.
    """

    def __init__(self, graph):
        """Initializes the GraphVisualizer with a given graph.

        Args:
            graph: A graph object compatible with OSMnx visualization.
        """
        self.graph = graph
        self.frames = []

    async def capture_frame(self):
        """Captures the current state of the graph as an image frame.

        This method generates a visualization of the graph using OSMnx,
        saves it as a temporary PNG image, and appends it to the frames list.

        Raises:
            ValueError: If the graph is invalid or not visualizable.
        """
        print(f"Capturing frame... (Frames before: {len(self.frames)})")

        fig, _ = ox.plot_graph(
            self.graph,
            node_size=[self.graph.nodes[node].get("size", 0) for node in self.graph.nodes],
            edge_color=[self.graph.edges[edge].get("color", "#2432B0") for edge in self.graph.edges],
            edge_alpha=0.3,
            edge_linewidth=[self.graph.edges[edge].get("linewidth", 0.5) for edge in self.graph.edges],
            node_color="#ADD8E6",
            bgcolor="#0F1126",
            show=False,
            close=False
        )

        buf = BytesIO()
        plt.savefig(buf, format='png', dpi=300)
        buf.seek(0)
        img = Image.open(buf).copy()
        buf.close()
        plt.close(fig)

        self.frames.append(img)
        print(f"Frame captured! (Total frames: {len(self.frames)})")

    def save_gif(self, gif_filename: str, duration: int = 100):
        """Generates a GIF from the captured frames.

        This method compiles all captured image frames into an animated
        GIF and saves it to the specified file location.

        Args:
            gif_filename (str): The name of the output GIF file.
            duration (int): Duration of each frame in milliseconds. Defaults to 100.

        Raises:
            FileNotFoundError: If the directory for saving the GIF does not exist
                and cannot be created.
            ValueError: If no frames are available to save.
        """
        print(f"Saving GIF... (Frames: {len(self.frames)})")

        if self.frames:
            output_dir = os.path.join("results", "animations")
            os.makedirs(output_dir, exist_ok=True)
            full_path = os.path.join(output_dir, gif_filename)

            self.frames[0].save(
                full_path,
                save_all=True,
                append_images=self.frames[1:],
                duration=duration,
                loop=0
            )
            print(f"✅ GIF saved: {full_path}")
        else:
            print("⚠️ No frames to save! GIF not created.")
