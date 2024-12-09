"""Test file for implemented algorithms and graph."""

from graph_utils import initialize_graph, GraphProcessor, GraphStyler, GraphVisualizer
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm


def test_initialize_graph():
    """Tests graph initialization - graph, nodes, and edges must exist."""
    graph = initialize_graph("Gliwice, Poland")
    assert graph is not None, "Graph not initialized."
    assert len(graph.nodes) > 0, "Graph must have nodes."
    assert len(graph.edges) > 0, "Graph must have edges."


def test_bfs_algorithm():
    """Tests BFS algorithm - end point must be reached."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    # Initialize nodes and edges
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    bfs = BFSAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    print(f"Start: {start}, End: {end}")
    bfs.execute(start, end)

    assert graph.nodes[end]["visited"], "BFS failed to visit the end node."



def test_dijkstra_algorithm():
    """Tests Dijkstra algorithm - end point must not have infinite cost."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    # Initialize nodes and edges
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    dijkstra = DijkstraAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    dijkstra.execute(start, end)
    assert graph.nodes[end]["distance"] < float("inf"), "Dijkstra failed to find a path."


def test_astar_algorithm():
    """Tests A* algorithm - end point must not have infinite cost."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    # Initialize nodes and edges
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    astar = AStarAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    astar.execute(start, end)
    assert graph.nodes[end]["f_score"] < float("inf"), "A* failed to find a path."


# Additional Tests

def test_revisit_prevention_bfs():
    """Ensure BFS does not revisit already visited nodes."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    bfs = BFSAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    bfs.execute(start, end)
    visited_nodes = [node for node in graph.nodes if graph.nodes[node]["visited"]]
    assert len(visited_nodes) > 0, "No nodes visited during BFS."
    assert len(set(visited_nodes)) == len(visited_nodes), "BFS revisited a node."


def test_shortest_path_dijkstra():
    """Ensure Dijkstra finds the shortest path."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    dijkstra = DijkstraAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    dijkstra.execute(start, end)

    # Reconstruct the path and calculate its total weight
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = graph.nodes[current]["previous"]
    path.reverse()

    path_weight = sum(graph.edges[(path[i], path[i + 1], 0)]["weight"] for i in range(len(path) - 1))
    assert path_weight == graph.nodes[end]["distance"], "Dijkstra did not find the shortest path."


def test_heuristic_astar():
    """Ensure A* heuristic is consistent with expected results."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    astar = AStarAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    astar.execute(start, end)
    heuristic_start_to_end = astar._heuristic(start, end)
    assert heuristic_start_to_end > 0, "Heuristic value should be greater than 0."
    assert heuristic_start_to_end < float("inf"), "Heuristic value should not be infinite."


def test_graph_connectivity():
    """Ensure the graph is connected, allowing traversal between start and end."""
    graph = initialize_graph("Gliwice, Poland")
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    # Perform BFS or any algorithm to check connectivity
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()
    bfs = BFSAlgorithm(graph, visualizer, styler)

    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    bfs.execute(start, end)
    assert graph.nodes[end]["visited"], "Graph is not connected (no path from start to end)."
