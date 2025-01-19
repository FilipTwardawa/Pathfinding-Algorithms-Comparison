# A* Algorithm

## Overview
The A* algorithm is a graph traversal and pathfinding algorithm. It finds the shortest path between a start node and a goal node using:
- A **heuristic function** (e.g., Euclidean distance) to estimate the cost to reach the goal.
- The cost of the path already traveled.

## How It Works
1. Start at the given node, calculate the total cost `f(n) = g(n) + h(n)`:
   - `g(n)` is the cost from the start to the current node.
   - `h(n)` is the heuristic estimate from the current node to the target.
2. Expand the node with the smallest `f(n)`.
3. Repeat until the goal node is reached.

## Performance
- **Time Complexity**: O((E + V) * log(V)), where E is edges and V is vertices.
- **Space Complexity**: O(V), for maintaining the priority queue.

## Example Code
```python
from algorithms import AStarAlgorithm

# Initialize algorithm
algorithm = AStarAlgorithm(graph, visualizer, styler)

# Execute the algorithm
algorithm.execute(start_node, end_node)
