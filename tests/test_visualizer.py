import pytest
from core.graph_visualizer import GraphVisualizer
from utils.graph_initializer import initialize_graph
from PIL import Image
import os


@pytest.mark.asyncio
async def test_visualizer_capture_frame():
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)

    await visualizer.capture_frame()
    assert len(visualizer.frames) == 1, "Failed to register graph frame"


def test_visualizer_save_gif():
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)

    fake_image = Image.new("RGB", (100, 100), color="white")
    visualizer.frames = [fake_image] * 5

    visualizer.save_gif("test.gif")

    output_dir = os.path.join("results", "animations")
    full_path = os.path.join(output_dir, "test.gif")
    assert os.path.exists(full_path), "GIF has not been saved"
