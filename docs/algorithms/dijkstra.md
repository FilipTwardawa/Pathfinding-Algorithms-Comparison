# Dijkstra's Algorithm

## Overview
Dijkstra's Algorithm is a widely used pathfinding algorithm that calculates the shortest path from a source node to all other nodes in a graph. It works with **non-negative edge weights** and guarantees optimal results for both directed and undirected graphs.

The algorithm is suitable for:
- Finding the shortest path in weighted graphs.
- Applications in navigation systems, network routing, and more.

---

## How It Works
1. **Initialization**:
   - Assign a tentative distance of `0` to the source node and `infinity` to all other nodes.
   - Add the source node to a priority queue.

2. **Node Processing**:
   - Extract the node with the smallest distance from the priority queue.
   - For each neighbor of the current node:
     - Calculate the tentative distance through the current node.
     - If the new distance is shorter, update it and set the current node as the predecessor.
     - Add the neighbor to the priority queue if not already processed.

3. **Termination**:
   - The algorithm ends when:
     - All nodes are processed.
     - The target node (if specified) is reached.

---

## Complexity
- **Time Complexity**: O((E + V) * log(V)), where:
  - `V` = Number of vertices (nodes).
  - `E` = Number of edges.
  - The log(V) factor comes from priority queue operations.
- **Space Complexity**: O(V), for storing distances, predecessors, and the priority queue.

---

## Example Code
Here’s how to use the Dijkstra algorithm within the framework:

```python
from algorithms import DijkstraAlgorithm

# Initialize the algorithm
algorithm = DijkstraAlgorithm(graph, visualizer, styler)

# Define the start and end nodes
start_node = 1
end_node = 10

# Execute the algorithm
await algorithm.execute(start_node, end_node, plot=True)

# After execution, reconstruct the shortest path
reconstructed_path = []
current_node = end_node
while current_node is not None:
    reconstructed_path.append(current_node)
    current_node = graph.nodes[current_node]["previous"]
reconstructed_path.reverse()

print(f"Shortest Path: {reconstructed_path}")
