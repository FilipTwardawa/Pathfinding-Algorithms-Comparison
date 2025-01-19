# Algorithms Module

## Overview

The `algorithms` module implements the core pathfinding algorithms used in this project. Each algorithm is designed to operate on a graph structure and is responsible for computing the optimal path between two nodes.

### Key Features
- Modular implementation of popular pathfinding algorithms:
  - **Dijkstra's Algorithm**: Guarantees the shortest path in weighted graphs.
  - **A* Algorithm**: Combines heuristics with path cost for efficient traversal.
  - **Breadth-First Search (BFS)**: Explores all nodes at the current depth before moving deeper (ideal for unweighted graphs).
- Asynchronous execution for efficient performance.
- Integration with graph styling and visualization tools to produce animations and metrics.

### Algorithms Implemented
1. **Dijkstra's Algorithm**: 
   - Best for weighted graphs where all edge weights are non-negative.
   - Complexity: \(O((V + E) \cdot \log V)\).

2. **A* Algorithm**:
   - Enhances Dijkstra by incorporating a heuristic function (e.g., Euclidean distance).
   - Optimized for shortest pathfinding in spatial graphs.

3. **BFS**:
   - Ideal for unweighted graphs or simple reachability checks.
   - Complexity: \(O(V + E)\).

### Extensibility
This module is designed to support additional algorithms. To add a new algorithm:
1. Create a new Python file in the `algorithms/` directory.
2. Implement the `GraphAlgorithm` interface.
3. Add the algorithm to the `AlgorithmComparator`.
