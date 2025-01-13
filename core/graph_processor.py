class GraphProcessor:
    """Processes vertices and edges in a graph."""

    @staticmethod
    def initialize_nodes(graph):
        """Resets the state of the vertices and their metadata."""
        for node in graph.nodes:
            graph.nodes[node].update({
                "visited": False,
                "previous": None,
                "size": 0,
                "distance": float("inf"),
                "g_score": float("inf"),
                "f_score": float("inf")
            })

    @staticmethod
    def initialize_edges(graph, styler):
        """Resets edge styling."""
        for edge in graph.edges:
            styler.style_edge(graph, edge)
