class GraphProcessor:
    """
    Provides utility methods to process and manage nodes and edges in a graph.

    This class contains static methods to initialize the properties of graph nodes
    and edges, ensuring they are reset to a defined default state.
    """

    @staticmethod
    def initialize_nodes(graph):
        """
        Reset the state of all nodes in the given graph.

        Args:
            graph (networkx.Graph): A graph object where nodes are being reset.
                The graph is expected to be compatible with NetworkX or a similar
                library providing a 'nodes' attribute.

        Updates:
            - `graph.nodes[node]["visited"]` (bool): Set to `False`, indicating
              the node has not been visited.
            - `graph.nodes[node]["previous"]` (Any): Set to `None`, clearing
              the previous node reference.
            - `graph.nodes[node]["size"]` (int): Set to `0`, resetting size metadata.
            - `graph.nodes[node]["distance"]` (float): Set to infinity
              (`float("inf")`), resetting the distance metric.
            - `graph.nodes[node]["g_score"]` (float): Set to infinity
              (`float("inf")`), resetting the g-score.
            - `graph.nodes[node]["f_score"]` (float): Set to infinity
              (`float("inf")`), resetting the f-score.

        Returns:
            None
        """
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
        """
        Reset the styles of all edges in the given graph.

        Args:
            graph (networkx.Graph): A graph object where edges are being reset.
                The graph should support an 'edges' attribute.
            styler (object): An object that provides a `style_edge(graph, edge)`
                method to apply the required styling logic for each edge.

        Updates:
            Calls `styler.style_edge(graph, edge)` for each edge in the graph.

        Returns:
            None
        """
        for edge in graph.edges:
            styler.style_edge(graph, edge)
