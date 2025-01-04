"""
Example File Using Implemented Algorithms to Compare Results

This module creates a graph and runs three pathfinding algorithms (BFS, Dijkstra, A*)
to compare their performance in terms of path, cost, execution time, and visited nodes.
"""

from graph_utils import initialize_graph_with_distant_points, GraphStyler, GraphProcessor
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm

def main():
    """
    Main function to initialize a graph and run pathfinding algorithms.

    This function generates a graph for Warsaw, Poland, selects two distant points,
    and runs BFS, Dijkstra, and A* algorithms on the graph. The results of each
    algorithm are printed for comparison.
    """
    # Initialize the graph and select start and end nodes
    graph, start_node, end_node = initialize_graph_with_distant_points("Warsaw, Poland")

    # Initialize styling objects
    styler = GraphStyler()

    print(f"Start: {graph.nodes[start_node]['name']}, End: {graph.nodes[end_node]['name']}")

    # Initialize nodes and edges in the graph
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # Run BFS
    print("Running BFS...")
    bfs = BFSAlgorithm(graph, None, styler)
    result_b = bfs.execute(start_node, end_node, plot=False)
    print("BFS completed.")

    # Reinitialize nodes and edges for the next algorithm
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # Run Dijkstra
    print("Running Dijkstra...")
    dijkstra = DijkstraAlgorithm(graph, None, styler)
    result_d = dijkstra.execute(start_node, end_node, plot=False)
    print("Dijkstra completed.")

    # Reinitialize nodes and edges for the next algorithm
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    # Run A*
    print("Running A*...")
    astar = AStarAlgorithm(graph, None, styler)
    result_a = astar.execute(start_node, end_node, plot=False)
    print("A* completed.")

    # Print BFS results
    print("\nBFS Results:")
    print(f"Path: {result_b[0]}")
    print(f"Cost: {result_b[1]}")
    print(f"Time: {result_b[2]:.4f} seconds")
    print(f"Path Steps: {result_b[3]}")
    print(f"Visited Nodes: {result_b[4]}")

    # Print Dijkstra results
    print("\nDijkstra Results:")
    print(f"Path: {result_d[0]}")
    print(f"Cost: {result_d[1]}")
    print(f"Time: {result_d[2]:.4f} seconds")
    print(f"Path Steps: {result_d[3]}")
    print(f"Visited Nodes: {result_d[4]}")

    # Print A* results
    print("\nA* Results:")
    print(f"Path: {result_a[0]}")
    print(f"Cost: {result_a[1]}")
    print(f"Time: {result_a[2]:.4f} seconds")
    print(f"Path Steps: {result_a[3]}")
    print(f"Visited Nodes: {result_a[4]}")

    print("\nAll algorithms completed.")

if __name__ == "__main__":
    main()
