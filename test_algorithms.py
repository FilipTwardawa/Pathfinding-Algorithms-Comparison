"""Test file for implemented algorithms and graph."""
# import pytest
from graph_utils import initialize_graph, GraphProcessor, GraphStyler, GraphVisualizer
from algorithms import BFSAlgorithm, DijkstraAlgorithm, AStarAlgorithm


def test_initialize_graph():
    """Tests graph initation - graph, nodes and edges must exist."""
    graph = initialize_graph("Gliwice, Poland")
    assert graph is not None
    assert len(graph.nodes) > 0
    assert len(graph.edges) > 0


def test_bfs_algorithm():
    """Tests BFS algorithm - end point must be reached."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    # Inicjalizacja węzłów przed uruchomieniem algorytmu
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    bfs = BFSAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    bfs.execute(start, end)
    assert graph.nodes[end]["visited"]  # Sprawdzenie, czy węzeł końcowy został odwiedzony


def test_dijkstra_algorithm():
    """Tests Dijkstra algorithm - end point must not have infinite cost."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    # Inicjalizacja węzłów przed uruchomieniem algorytmu
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    dijkstra = DijkstraAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    dijkstra.execute(start, end)
    assert graph.nodes[end]["distance"] < float("inf")  # Sprawdzenie, czy znaleziono ścieżkę


def test_astar_algorithm():
    """Tests A* algorithm - end point must not have infinite cost."""
    graph = initialize_graph("Gliwice, Poland")
    visualizer = GraphVisualizer(graph)
    styler = GraphStyler()

    # Inicjalizacja węzłów przed uruchomieniem algorytmu
    GraphProcessor.initialize_nodes(graph)
    GraphProcessor.initialize_edges(graph, styler)

    astar = AStarAlgorithm(graph, visualizer, styler)
    start = list(graph.nodes)[0]
    end = list(graph.nodes)[-1]

    astar.execute(start, end)
    assert graph.nodes[end]["f_score"] < float("inf")  # Sprawdzenie, czy znaleziono ścieżkę
