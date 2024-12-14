"""Example file using implemented algorithms."""
import random
from graph_utils import initialize_graph, GraphStyler, GraphProcessor, GraphVisualizer
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm, PathReconstructor


def main():
    """Creates an example graph and runs pathfinding algorithms."""
    # Ustawienie miejsca, dla którego generujemy graf
    place_name = "Gliwice, Poland"
    graph = initialize_graph(place_name)

    # Inicjalizacja obiektów do stylizacji i wizualizacji
    styler = GraphStyler()
    visualizer = GraphVisualizer(graph)

    # Losowy wybór węzłów startowego i końcowego
    start = random.choice(list(graph.nodes))
    end = random.choice(list(graph.nodes))
    print(f"Start: {start}, End: {end}")

    # Inicjalizacja węzłów i krawędzi grafu
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # BFS
    print("Running BFS...")
    bfs = BFSAlgorithm(graph, visualizer, styler)
    result_b = bfs.execute(start, end, plot=True)
    reconstructor = PathReconstructor(graph, visualizer, styler)
    reconstructor.reconstruct_path(start, end, plot=True)
    visualizer.save_gif("bfs_animation.gif")
    print("BFS completed. Animation saved as 'bfs_animation.gif'.")

    # Ponowna inicjalizacja węzłów i krawędzi
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # Dijkstra
    print("Running Dijkstra...")
    dijkstra = DijkstraAlgorithm(graph, visualizer, styler)
    result_d = dijkstra.execute(start, end, plot=True)
    reconstructor.reconstruct_path(start, end, plot=True)
    visualizer.save_gif("dijkstra_animation.gif")
    print("Dijkstra completed. Animation saved as 'dijkstra_animation.gif'.")

    # Ponowna inicjalizacja węzłów i krawędzi
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # A*
    print("Running A*...")
    astar = AStarAlgorithm(graph, visualizer, styler)
    result_a = astar.execute(start, end, plot=True)
    reconstructor.reconstruct_path(start, end, plot=True)
    visualizer.save_gif("astar_animation.gif")
    print("A* completed. Animation saved as 'astar_animation.gif'.")

    print(f"BFS path: {result_b[0]}")
    print(f"BFS cost: {result_b[1]}")
    print(f"BFS time: {result_b[2]}")
    print(f"Dijkstra path: {result_d[0]}")
    print(f"Dijkstra cost: {result_d[1]}")
    print(f"Dijkstra time: {result_d[2]}")
    print(f"A* path: {result_a[0]}")
    print(f"A* cost: {result_a[1]}")
    print(f"A* time: {result_a[2]}")


if __name__ == "__main__":
    main()
