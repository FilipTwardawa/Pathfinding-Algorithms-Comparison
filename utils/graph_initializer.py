import osmnx as ox


def initialize_graph(place_name: str):
    """
    Initializes a road network graph for a specified place using the osmnx library.

    This function creates a directed graph representing the road network of a given
    location. Node properties and edge weights are initialized to support routing
    and other graph-based computations.

    Args:
        place_name (str): The name of the place to generate the road network graph.
            This can be a city name, district, or any location recognized by OpenStreetMap (OSM).

    Returns:
        networkx.classes.multidigraph.MultiDiGraph: A directed graph object with initialized
            nodes and edges, ready for routing or graph-based analyses.

    Raises:
        ValueError: If the `place_name` does not correspond to a valid OSM location.

    Node Attributes:
        - visited (bool): Indicates if the node has been visited during graph traversal.
          Default is `False`.
        - previous (Any): Tracks the previous node in a path. Default is `None`.
        - size (int): Placeholder for node size, defaulting to `0`.
        - distance (float): Distance from the source node for shortest path computations.
          Default is set to infinity (`float('inf')`).
        - g_score (float): Cost to reach this node, used in A* or similar algorithms.
          Default is set to infinity (`float('inf')`).
        - f_score (float): Estimated total cost to reach the target node from this node.
          Default is set to infinity (`float('inf')`).

    Edge Attributes:
        - maxspeed (int): Maximum speed on the edge. If not available in OSM data,
          defaults to `40`.
        - weight (float): Weight of the edge, calculated as length divided by maxspeed.

    Example:
        ```python
        import osmnx as ox

        graph = initialize_graph("Manhattan, New York, USA")
        print(graph)
        ```

    Note:
        - The function assumes `network_type="drive"` to filter for drivable paths.
        - If the `maxspeed` attribute is missing or not a valid integer, a default value
          of `40` is applied.
    """
    graph = ox.graph_from_place(place_name, network_type="drive")

    # Initialize nodes with default values
    for node in graph.nodes:
        graph.nodes[node].update({
            "visited": False,
            "previous": None,
            "size": 0,
            "distance": float("inf"),
            "g_score": float("inf"),
            "f_score": float("inf"),
        })

    # Edge initialization
    for edge in graph.edges:
        maxspeed = 40
        if "maxspeed" in graph.edges[edge]:
            maxspeed_value = graph.edges[edge]["maxspeed"]
            if isinstance(maxspeed_value, str) and maxspeed_value.isdigit():
                maxspeed = int(maxspeed_value)
        weight = graph.edges[edge]["length"] / maxspeed
        graph.edges[edge].update({
            "maxspeed": maxspeed,
            "weight": weight,
        })

    return graph
