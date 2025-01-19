class GraphStyler:
    """Handles styling of graph elements, including nodes and edges.

    This class provides static methods to apply specific styles to nodes and edges
    in a graph. The styles include color, transparency, line width for edges,
    and size for nodes.
    """

    @staticmethod
    def style_edge(graph, edge, color="#2432B0", alpha=0.3, linewidth=0.5):
        """Applies styling to a specific edge in the graph.

        If the edge exists in the graph, this method updates its properties
        with the specified color, transparency, and line width.

        Args:
            graph (networkx.Graph): The graph containing the edges.
            edge (tuple): A tuple representing the edge (source, target).
            color (str, optional): Hexadecimal or named color for the edge. Defaults to "#2432B0".
            alpha (float, optional): Transparency level of the edge (0 to 1). Defaults to 0.3.
            linewidth (float, optional): Width of the edge line. Defaults to 0.5.

        Returns:
            None: The function modifies the graph in place and does not return a value.
        """
        if edge not in graph.edges:
            return
        graph.edges[edge].update({"color": color, "alpha": alpha, "linewidth": linewidth})

    @staticmethod
    def style_node(graph, node: int, size: int):
        """Sets the style for a specific node in the graph.

        This method updates the size property of the specified node.

        Args:
            graph (networkx.Graph): The graph containing the nodes.
            node (int): The identifier of the node to style.
            size (int): The size to assign to the node.

        Returns:
            None: The function modifies the graph in place and does not return a value.
        """
        graph.nodes[node]["size"] = size
