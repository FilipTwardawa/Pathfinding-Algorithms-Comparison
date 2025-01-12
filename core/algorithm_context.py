from abc import ABC, abstractmethod


class GraphAlgorithm(ABC):
    """An abstract base class for graph algorithms."""

    def __init__(self, graph, visualizer, styler):
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    @abstractmethod
    def execute(self, start: int, end: int, plot: bool = False):
        """It performs the algorithm."""
        pass

    def initialize_graph(self):
        """Initializes vertices and edges in a graph."""
        from core.graph_processor import GraphProcessor

        GraphProcessor.initialize_nodes(self.graph)
        GraphProcessor.initialize_edges(self.graph, self.styler)
