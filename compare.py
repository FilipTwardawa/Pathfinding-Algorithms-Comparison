"""Example file using implemented algorithms to compare results."""
from graph_utils import initialize_graph_with_distant_points, GraphStyler, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm


def main():
    """Creates an example graph and runs pathfinding algorithms."""
    # Inicjalizacja grafu i węzłów startowych/końcowych
    graph, start_node, end_node = initialize_graph_with_distant_points("Warsaw, Poland")

    # Inicjalizacja obiektów do stylizacji
    styler = GraphStyler()

    print(f"Start: {graph.nodes[start_node]['name']}, End: {graph.nodes[end_node]['name']}")

    # Inicjalizacja węzłów i krawędzi grafu
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # BFS
    print("Running BFS...")
    bfs = BFSAlgorithm(graph, None, styler)
    result_b = bfs.execute(start_node, end_node, plot=False)
    print("BFS completed.")

    # Ponowna inicjalizacja węzłów i krawędzi
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # Dijkstra
    print("Running Dijkstra...")
    dijkstra = DijkstraAlgorithm(graph, None, styler)
    result_d = dijkstra.execute(start_node, end_node, plot=False)
    print("Dijkstra completed.")

    # Ponowna inicjalizacja węzłów i krawędzi
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # A*
    print("Running A*...")
    astar = AStarAlgorithm(graph, None, styler)
    result_a = astar.execute(start_node, end_node, plot=False)
    print("A* completed.")

    print("BFS results: ")
    print(f"BFS path: {result_b[0]}")
    print(f"BFS cost: {result_b[1]}")
    print(f"BFS time: {result_b[2]}")
    print(f"BFS path steps: {result_b[3]}")
    print(f"BFS visited nodes: {result_b[4]}")

    print("Dijkstra results: ")
    print(f"Dijkstra path: {result_d[0]}")
    print(f"Dijkstra cost: {result_d[1]}")
    print(f"Dijkstra time: {result_d[2]}")
    print(f"Dijkstra path steps: {result_d[3]}")
    print(f"Dijkstra visited nodes: {result_d[4]}")

    print("A* results: ")
    print(f"A* path: {result_a[0]}")
    print(f"A* cost: {result_a[1]}")
    print(f"A* time: {result_a[2]}")
    print(f"A* path steps: {result_a[3]}")
    print(f"A* visited nodes: {result_a[4]}")

    print("All algorithms completed.")


if __name__ == "__main__":
    main()
