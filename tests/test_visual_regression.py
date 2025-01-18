import pytest
from core import GraphVisualizer
from utils import initialize_graph
from PIL import Image, ImageChops
import os


@pytest.mark.asyncio
async def test_visual_regression():
    """
    Test for visual regression in the GraphVisualizer.

    This test initializes a graph based on the location "Gliwice, Poland" and
    uses the GraphVisualizer to generate a visualization. The generated frame
    is compared with a reference image to ensure no regressions in visualization.

    Steps:
        1. Initialize the graph for a specified location.
        2. Capture a frame using the GraphVisualizer.
        3. Check if a reference image exists:
            - If missing, create a new reference image and skip the test.
        4. Compare the generated image with the reference image using pixel difference.

    Raises:
        AssertionError: If there are visual differences between the generated and reference images.
    """
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)

    await visualizer.capture_frame()

    # Path to the reference file
    reference_path = "tests/expected_frame.png"

    # Create a directory if it does not exist
    os.makedirs(os.path.dirname(reference_path), exist_ok=True)

    if not os.path.exists(reference_path):
        print(f"Reference file missing. I am creating a new one: {reference_path}")
        generated_image = visualizer.frames[0]
        generated_image.save(reference_path)
        pytest.skip(f"A reference file has been created: {reference_path}. Run the test again.")

    # Image comparison
    expected_image = Image.open(reference_path)
    generated_image = visualizer.frames[0]
    diff = ImageChops.difference(expected_image, generated_image)

    assert diff.getbbox() is None, "Changes in visualization introduced regression"
