# Core Module

## Overview

The `core` module is the backbone of the application. It provides the foundational components for managing, processing, and comparing pathfinding algorithms. This module also includes utilities for handling feature flags, commands, and graph visualization.

### Key Features
1. **Algorithm Comparator**:
   - Facilitates the comparison of pathfinding algorithms by running them on the same graph and collecting metrics like time, cost, and path length.
2. **Graph Processing**:
   - Handles initialization and resetting of graph nodes and edges.
   - Ensures consistent graph states before algorithm execution.
3. **Visualization and Styling**:
   - Tools to style and visualize graph components (nodes, edges, and paths).
   - Generates animations (GIFs) and comparison charts.
4. **Dependency Management**:
   - Simplifies integration and testing through dependency injection.
5. **Feature Flags**:
   - Dynamically enables or disables features using a Flagsmith-based configuration.

### Key Components
1. **`algorithm_comparator.py`**:
   - Manages algorithm execution, metric collection, and visualization.
2. **`graph_processor.py`**:
   - Initializes graph nodes and edges with default properties.
3. **`graph_visualizer.py`**:
   - Creates visualizations and animations for algorithms in action.
4. **`path_reconstructor.py`**:
   - Reconstructs the computed path and styles it for visualization.

### Integration
The `core` module interacts seamlessly with other modules, including:
- **Algorithms Module**: Provides the algorithms for comparison.
- **Utilities Module**: Supplies initialization logic for graphs.
