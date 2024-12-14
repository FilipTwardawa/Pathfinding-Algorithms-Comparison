"""Example file using implemented algorithms to compare results."""
import random
from graph_utils import initialize_graph, GraphStyler, GraphProcessor, GraphVisualizer
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm


def main():
    """Creates an example graph and runs pathfinding algorithms."""
    # Ustawienie miejsca, dla którego generujemy graf
    place = "Gliwice, Poland"
    graph = initialize_graph(place)

    # Inicjalizacja obiektów do stylizacji i wizualizacji
    styler = GraphStyler()
    visualizer = GraphVisualizer(graph)

    # Losowy wybór węzłów startowego i końcowego
    start_node = random.choice(list(graph.nodes))
    end_node = random.choice(list(graph.nodes))
    print(f"Start: {start_node}, End: {end_node}")

    # Inicjalizacja węzłów i krawędzi grafu
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # BFS
    print("Running BFS...")
    bfs = BFSAlgorithm(graph, visualizer, styler)
    result_b = bfs.execute(start_node, end_node, plot=False)
    print("BFS completed.")

    # Ponowna inicjalizacja węzłów i krawędzi
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # Dijkstra
    print("Running Dijkstra...")
    dijkstra = DijkstraAlgorithm(graph, visualizer, styler)
    result_d = dijkstra.execute(start_node, end_node, plot=False)
    print("Dijkstra completed.")

    # Ponowna inicjalizacja węzłów i krawędzi
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # A*
    print("Running A*...")
    astar = AStarAlgorithm(graph, visualizer, styler)
    result_a = astar.execute(start_node, end_node, plot=False)
    print("A* completed.")

    print("BFS results: ")
    print(f"BFS path: {result_b[0]}")
    print(f"BFS cost: {result_b[1]}")
    print(f"BFS time: {result_b[2]}")

    print("Dijkstra results: ")
    print(f"Dijkstra path: {result_d[0]}")
    print(f"Dijkstra cost: {result_d[1]}")
    print(f"Dijkstra time: {result_d[2]}")

    print("A* results: ")
    print(f"A* path: {result_a[0]}")
    print(f"A* cost: {result_a[1]}")
    print(f"A* time: {result_a[2]}")

    print("All algorithms completed.")


if __name__ == "__main__":
    main()
