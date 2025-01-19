# Utilities Module

## Overview

The `utilities` module (`utils`) provides helper functions and utilities to simplify the core logic of the application. These utilities are designed to handle repetitive tasks, ensuring code modularity and reusability.

### Key Features
1. **Graph Initialization**:
   - Dynamically generates a graph using OpenStreetMap (OSM) data through the `osmnx` library.
   - Initializes node and edge attributes for use in pathfinding algorithms.
2. **Extensibility**:
   - Utility functions can be extended to support additional preprocessing tasks or graph types.

### Core Component
- **`graph_initializer.py`**:
  - Contains the `initialize_graph` function, which creates a directed graph from a specified location (e.g., "Gliwice, Poland").
  - Prepares node attributes such as:
    - `distance` (set to infinity by default).
    - `visited` (boolean flag for traversal).
    - `size`, `g_score`, and `f_score` (used by A* and visualization tools).
  - Calculates edge weights based on `length` and `maxspeed`.

### Usage
The utilities in this module are critical for:
- Preprocessing graphs before algorithm execution.
- Ensuring that the graph is in a consistent state.