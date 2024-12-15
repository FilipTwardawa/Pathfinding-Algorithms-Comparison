"""File using implemented algorithms to make plots."""
import matplotlib.pyplot as plt
from graph_utils import initialize_graph_with_distant_points, GraphStyler, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm


def plot_comparisons(results, save_path=None):
    """Create enhanced bar charts for cost and execution time comparisons."""
    # Extract data
    algorithms = list(results.keys())
    costs = [results[algo]["cost"] for algo in algorithms]
    times = [results[algo]["time"] for algo in algorithms]
    depths = [results[algo]["depth"] for algo in algorithms]
    visited = [results[algo]["visited"] for algo in algorithms]

    # Plot costs
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, costs, color=["blue", "green", "orange"])
    plt.title("Porównanie Kosztów", fontsize=16)
    plt.ylabel("Koszt całkowity", fontsize=12)
    plt.xlabel("Algorytmy", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Add values on top of bars
    for ba in bars:
        plt.text(
            ba.get_x() + ba.get_width() / 2,
            ba.get_height(),
            f"{ba.get_height():.2f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    # Save chart if save_path is provided
    if save_path:
        plt.savefig(f"{save_path}_costs.png", dpi=300)
        print(f"Cost comparison chart saved as {save_path}_costs.png")

    plt.show()

    # Plot execution times
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, times, color=["blue", "green", "orange"])
    plt.title("Porównanie Czasu Wykonania", fontsize=16)
    plt.ylabel("Czas (sekundy)", fontsize=12)
    plt.xlabel("Algorytmy", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Add values on top of bars
    for ba in bars:
        plt.text(
            ba.get_x() + ba.get_width() / 2,
            ba.get_height(),
            f"{ba.get_height():.4f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    # Save chart if save_path is provided
    if save_path:
        plt.savefig(f"{save_path}_times.png", dpi=300)
        print(f"Time comparison chart saved as {save_path}_times.png")

    plt.show()

    # Plot path lengths
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, depths, color=["blue", "green", "orange"])
    plt.title("Liczba kroków do celu", fontsize=16)
    plt.ylabel("Liczba kroków", fontsize=12)
    plt.xlabel("Algorytmy", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Add values on top of bars
    for ba in bars:
        plt.text(
            ba.get_x() + ba.get_width() / 2,
            ba.get_height(),
            f"{ba.get_height():.4f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    # Save chart if save_path is provided
    if save_path:
        plt.savefig(f"{save_path}_depths.png", dpi=300)
        print(f"Step count comparison chart saved as {save_path}_depths.png")

    plt.show()

    # Plot count of visited nodes
    plt.figure(figsize=(10, 6))
    bars = plt.bar(algorithms, visited, color=["blue", "green", "orange"])
    plt.title("Porównanie liczby odwiedzonych punktów", fontsize=16)
    plt.ylabel("Liczba odwiedzonych punktów", fontsize=12)
    plt.xlabel("Algorytmy", fontsize=12)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # Add values on top of bars
    for ba in bars:
        plt.text(
            ba.get_x() + ba.get_width() / 2,
            ba.get_height(),
            f"{ba.get_height():.4f}",
            ha="center",
            va="bottom",
            fontsize=10,
            color="black",
        )

    # Save chart if save_path is provided
    if save_path:
        plt.savefig(f"{save_path}_visited_nodes.png", dpi=300)
        print(f"Count of visited nodes comparison chart saved as {save_path}_visited_nodes.png")

    plt.show()


def main():
    """Creates an example graph and runs pathfinding algorithms with visualizations."""
    # Inicjalizacja grafu i węzłów startowych/końcowych
    graph, start_node, end_node = initialize_graph_with_distant_points("Warsaw, Poland")

    # Inicjalizacja obiektów do stylizacji
    styler = GraphStyler()

    print(f"Start: {graph.nodes[start_node]['name']}, End: {graph.nodes[end_node]['name']}")

    # Przechowuje wyniki algorytmów
    results = {}

    # BFS
    print("Running BFS algorithm...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    bfs = BFSAlgorithm(graph, None, styler)
    result_b = bfs.execute(start_node, end_node, plot=False)
    results["BFS"] = {"path": result_b[0], "cost": result_b[1], "time": result_b[2],
                      "depth": result_b[3], "visited": result_b[4]}
    print("BFS completed.")

    # Dijkstra
    print("Running Dijkstra algorithm...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    dijkstra = DijkstraAlgorithm(graph, None, styler)
    result_d = dijkstra.execute(start_node, end_node, plot=False)
    results["Dijkstra"] = {"path": result_d[0], "cost": result_d[1], "time": result_d[2],
                           "depth": result_d[3], "visited": result_d[4]}
    print("Dijkstra completed.")

    # A*
    print("Running A* algorithm...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    astar = AStarAlgorithm(graph, None, styler)
    result_a = astar.execute(start_node, end_node, plot=False)
    results["A*"] = {"path": result_a[0], "cost": result_a[1], "time": result_a[2],
                     "depth": result_a[3], "visited": result_a[4]}
    print("A* completed.")

    # Visualize comparisons and save charts
    plot_comparisons(results, save_path="algorithm_comparison")


if __name__ == "__main__":
    main()
