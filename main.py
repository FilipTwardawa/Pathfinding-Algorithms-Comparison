import matplotlib.pyplot as plt
from graph_utils import initialize_graph_with_distant_points, GraphStyler, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm

def plot_comparisons(results, save_path=None):
    """Create enhanced bar charts for cost and execution time comparisons."""
    # Extract data
    algorithms = list(results.keys())
    costs = [results[algo]["cost"] for algo in algorithms]
    times = [results[algo]["time"] for algo in algorithms]

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
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{bar.get_height():.2f}",
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
    for bar in bars:
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{bar.get_height():.4f}",
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

def main():
    """Creates an example graph and runs pathfinding algorithms with visualizations."""
    # Inicjalizacja grafu i węzłów startowych/końcowych
    graph, start_node, end_node = initialize_graph_with_distant_points("Warsaw, Poland")

    # Inicjalizacja obiektów do stylizacji
    styler = GraphStyler()

    print(f"Start: {start_node}, End: {end_node}")

    # Przechowuje wyniki algorytmów
    results = {}

    # BFS
    print("Running BFS...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    bfs = BFSAlgorithm(graph, None, styler)
    result_b = bfs.execute(start_node, end_node, plot=False)
    results["BFS"] = {"path": result_b[0], "cost": result_b[1], "time": result_b[2]}
    print("BFS completed.")

    # Dijkstra
    print("Running Dijkstra...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    dijkstra = DijkstraAlgorithm(graph, None, styler)
    result_d = dijkstra.execute(start_node, end_node, plot=False)
    results["Dijkstra"] = {"path": result_d[0], "cost": result_d[1], "time": result_d[2]}
    print("Dijkstra completed.")

    # A*
    print("Running A*...")
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)
    astar = AStarAlgorithm(graph, None, styler)
    result_a = astar.execute(start_node, end_node, plot=False)
    results["A*"] = {"path": result_a[0], "cost": result_a[1], "time": result_a[2]}
    print("A* completed.")

    # Visualize comparisons and save charts
    plot_comparisons(results, save_path="algorithm_comparison")

if __name__ == "__main__":
    main()
