# Breadth-First Search (BFS)

## Overview
Breadth-First Search (BFS) is a graph traversal algorithm that explores all neighbors of a node before moving to the next level of nodes. It guarantees finding the shortest path in **unweighted graphs** but is not suitable for weighted graphs.

## How It Works
1. **Initialization**: Start with the source node and mark it as visited.
2. **Queue-Based Traversal**: Use a queue to process nodes level by level:
   - Dequeue the front node.
   - Visit all its unvisited neighbors and enqueue them.
3. **Termination**: The traversal ends when:
   - The target node is found (pathfinding mode).
   - All nodes are processed (full traversal).

## Complexity
- **Time Complexity**: O(V + E), where:
  - V = Number of vertices (nodes).
  - E = Number of edges.
- **Space Complexity**: O(V), for the visited nodes and the queue.

## Example Code
```python
from algorithms import BFSAlgorithm

# Initialize BFS algorithm
algorithm = BFSAlgorithm(graph, visualizer, styler)

# Execute BFS between start and end nodes
algorithm.execute(start_node, end_node)
