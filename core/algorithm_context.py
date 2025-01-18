from abc import ABC, abstractmethod


class GraphAlgorithm(ABC):
    """
    Abstract base class for graph algorithms.

    This class provides a framework for implementing graph-related algorithms. It ensures
    consistency and enforces a structure for derived classes to define core functionalities.

    Attributes:
        graph (Any): The data structure representing the graph (e.g., adjacency list, matrix).
        visualizer (Any): A visualization tool for graph processing and presentation.
        styler (Any): A styling object that configures the visual appearance of the graph.
    """

    def __init__(self, graph, visualizer, styler):
        """
        Constructs the GraphAlgorithm class instance.

        Args:
            graph (Any): The graph data structure on which the algorithm operates.
            visualizer (Any): A visualization tool for observing the graph processing.
            styler (Any): A styling object to customize the appearance of the graph visualization.
        """
        self.graph = graph
        self.visualizer = visualizer
        self.styler = styler

    @abstractmethod
    def execute(self, start: int, end: int, plot: bool = False):
        """
        Executes the specific graph algorithm.

        This method defines the primary logic that subclasses must implement. It applies
        the algorithm between the specified starting and ending nodes.

        Args:
            start (int): The starting node for the algorithm's computation.
            end (int): The target node for the algorithm's computation.
            plot (bool, optional): Whether to generate a visual representation of the graph
                after the algorithm execution. Defaults to False.

        Raises:
            NotImplementedError: If the method is not overridden in the subclass.
        """
        pass

    def initialize_graph(self):
        """
        Prepares the graph by initializing its nodes and edges.

        This method sets up the graph's vertices and edges to ensure it is in a valid
        and consistent state before executing any algorithm. It relies on the
        `GraphProcessor` class from the `core.graph_processor` module.

        Raises:
            ImportError: If the `GraphProcessor` module is not available or cannot be imported.
        """
        from core.graph_processor import GraphProcessor

        GraphProcessor.initialize_nodes(self.graph)
        GraphProcessor.initialize_edges(self.graph, self.styler)
