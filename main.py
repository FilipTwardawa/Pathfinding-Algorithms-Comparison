import cProfile
import pstats
import asyncio
import random
import time
from core import GraphProcessor, PathReconstructor
from core.graph_visualizer import GraphVisualizer
from core.graph_styler import GraphStyler
from utils.graph_initializer import initialize_graph
from algorithms.dijkstra import DijkstraAlgorithm
from algorithms.a_star import AStarAlgorithm
from algorithms.bfs import BFSAlgorithm
from core.algorithm_comparator import AlgorithmComparator

# Define a constant for the graph location
GRAPH_LOCATION = "Gliwice, Poland"


def profile_visualizer() -> None:
    """Profiles and generates GIFs for all pathfinding algorithms."""
    graph_instance = initialize_graph(GRAPH_LOCATION)
    styler = GraphStyler()
    visualizer = GraphVisualizer(graph_instance)
    start_node_instance = random.choice(list(graph_instance.nodes))
    end_node_instance = random.choice(list(graph_instance.nodes))

    # Ensure start and end nodes are distinct
    while start_node_instance == end_node_instance:
        end_node_instance = random.choice(list(graph_instance.nodes))

    # List of algorithms to profile
    algorithms = [
        ("Dijkstra", DijkstraAlgorithm(graph_instance, visualizer, styler)),
        ("A*", AStarAlgorithm(graph_instance, visualizer, styler)),
        ("BFS", BFSAlgorithm(graph_instance, visualizer, styler)),
    ]

    async def run_visualization():
        for name, algorithm in algorithms:
            print(f"Running {name} Algorithm...")
            try:
                await algorithm.execute(start_node_instance, end_node_instance, plot=True)
                print(f"{name} Algorithm finished successfully.")

                # Reconstruct the path and save GIF
                reconstructor = PathReconstructor(graph_instance, visualizer, styler)
                await reconstructor.reconstruct_path(start_node_instance, end_node_instance, plot=True)

                # Save GIF
                gif_filename = f"{name.lower()}_visualization.gif"
                await visualizer.save_gif(gif_filename, duration=100)
                print(f"Saved GIF for {name}: {gif_filename}")
            except Exception as error:
                print(f"Error during {name}: {error}")

            # Reset visualizer and graph for next algorithm
            visualizer.frames.clear()
            GraphProcessor.initialize_nodes(graph_instance)
            GraphProcessor.initialize_edges(graph_instance, styler)

    asyncio.run(run_visualization())


def compare_algorithms() -> None:
    """Compares algorithms and generates comparison visualizations."""
    graph_instance = initialize_graph(GRAPH_LOCATION)
    start_node_instance = random.choice(list(graph_instance.nodes))
    end_node_instance = random.choice(list(graph_instance.nodes))

    # Ensure start and end nodes are distinct
    while start_node_instance == end_node_instance:
        end_node_instance = random.choice(list(graph_instance.nodes))

    print(f"Selected start node: {start_node_instance}, end node: {end_node_instance}")

    comparator = AlgorithmComparator(graph_instance, start_node_instance, end_node_instance)
    comparator.run_comparison(plot=False)
    comparator.generate_visualizations()
    print("Comparison charts generated successfully.")


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()

    try:
        print("Starting visualizer profiling...")
        profile_visualizer()

        print("\nStarting algorithm comparison...")
        compare_algorithms()

    except Exception as e:
        print(f"Error during execution: {e}")

    profiler.disable()

    # Save profiler stats with a timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    profile_filename = f"main_profile_{timestamp}.prof"
    stats = pstats.Stats(profiler)
    stats.dump_stats(profile_filename)
    stats.sort_stats("time").print_stats(10)

    print(f"Profiler data saved to {profile_filename}")
