import pytest
from core import GraphVisualizer
from utils import initialize_graph
from PIL import Image
import os


@pytest.mark.asyncio
async def test_visualizer_capture_frame():
    """
    Test the ability of the GraphVisualizer to capture a frame.

    This ensures that after calling the `capture_frame` method, a single
    frame is successfully registered in the visualizer's frame list.

    Raises:
        AssertionError: If no frames are registered after capture.
    """
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)

    await visualizer.capture_frame()
    assert len(visualizer.frames) == 1, "Failed to register graph frame"


def test_visualizer_save_gif():
    """Test the ability of the GraphVisualizer to save frames as a GIF.

    This test initializes a graph and manually sets the frames of the
    `GraphVisualizer` instance to a list of fake images. It then invokes
    the `save_gif` method to save the frames as an animated GIF.
    The test verifies that the GIF is saved at the expected location.

    Raises:
        AssertionError: If the GIF file does not exist at the specified location.
    """
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)

    fake_image = Image.new("RGB", (100, 100), color="white")
    visualizer.frames = [fake_image] * 5

    visualizer.save_gif("test.gif")

    output_dir = os.path.join("results", "animations")
    full_path = os.path.join(output_dir, "test.gif")
    assert os.path.exists(full_path), "GIF has not been saved"
