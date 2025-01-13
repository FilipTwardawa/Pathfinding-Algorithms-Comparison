class GraphStyler:
    """Handles styling of graph elements (nodes and edges)."""

    @staticmethod
    def style_edge(graph, edge, color="#2432B0", alpha=0.3, linewidth=0.5):
        if edge not in graph.edges:
            return
        graph.edges[edge].update({"color": color, "alpha": alpha, "linewidth": linewidth})

    @staticmethod
    def style_node(graph, node: int, size: int):
        """Sets the style for a graph node."""
        graph.nodes[node]["size"] = size
