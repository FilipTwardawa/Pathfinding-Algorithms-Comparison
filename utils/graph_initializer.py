import osmnx as ox


def initialize_graph(place_name: str):
    """Initializes the graph and sets edge weights and node properties."""
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
