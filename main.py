import random
import asyncio
from core import FeatureFlagManager, FlagsmithProvider, GraphVisualizer, GraphStyler, GraphProcessor, \
    AlgorithmComparator, PathReconstructor
from utils.graph_initializer import initialize_graph
from algorithms import DijkstraAlgorithm, AStarAlgorithm, BFSAlgorithm
from credentials import flagsmith_api_key

# Initialize Feature Flags
flagsmith_provider = FlagsmithProvider(environment_key=flagsmith_api_key)
feature_flags = FeatureFlagManager(provider=flagsmith_provider)

# Define constants
GRAPH_LOCATION = "Gliwice, Poland"


async def profile_visualizer():
    """Profiles and generates GIFs for all pathfinding algorithms if enabled."""
    if not feature_flags.is_enabled("enable-visualizer"):
        print("Feature 'enable-visualizer' is disabled. Skipping visualization.")
        return

    graph_instance = initialize_graph(GRAPH_LOCATION)
    styler = GraphStyler()
    visualizer = GraphVisualizer(graph_instance)

    start_node = random.choice(list(graph_instance.nodes))
    end_node = random.choice(list(graph_instance.nodes))

    while start_node == end_node:
        end_node = random.choice(list(graph_instance.nodes))

    algorithms = [
        ("Dijkstra", DijkstraAlgorithm(graph_instance, visualizer, styler)),
        ("A*", AStarAlgorithm(graph_instance, visualizer, styler)),
        ("BFS", BFSAlgorithm(graph_instance, visualizer, styler)),
    ]

    async def run_visualization():
        for name, algorithm in algorithms:
            print(f"Running {name} Algorithm...")
            try:
                await algorithm.execute(start_node, end_node, plot=True)
                reconstructor = PathReconstructor(graph_instance, visualizer, styler)
                await reconstructor.reconstruct_path(start_node, end_node, plot=True)

                gif_filename = f"{name.lower()}_visualization.gif"
                await visualizer.save_gif(gif_filename, duration=100)
                print(f"Saved GIF for {name}: {gif_filename}")
            except Exception as error:
                print(f"Error during {name}: {error}")

            visualizer.frames.clear()
            GraphProcessor.initialize_nodes(graph_instance)
            GraphProcessor.initialize_edges(graph_instance, styler)

    await run_visualization()


def compare_algorithms():
    """Compares algorithms and generates comparison visualizations if enabled."""
    if not feature_flags.is_enabled("enable-algorithm-comparison"):
        print("Feature 'enable-algorithm-comparison' is disabled. Skipping comparison.")
        return

    graph_instance = initialize_graph(GRAPH_LOCATION)
    start_node = random.choice(list(graph_instance.nodes))
    end_node = random.choice(list(graph_instance.nodes))

    while start_node == end_node:
        end_node = random.choice(list(graph_instance.nodes))

    print(f"Selected start node: {start_node}, end node: {end_node}")

    comparator = AlgorithmComparator(graph_instance, start_node, end_node)
    comparator.run_comparison(plot=False)
    comparator.generate_visualizations()
    print("Comparison charts generated successfully.")


if __name__ == "__main__":
    print("Starting application...")


    # Check flags and execute features based on their states
    try:
        asyncio.run(profile_visualizer())
        compare_algorithms()
    except Exception as e:
        print(f"An error occurred during execution: {e}")
