# Pathfinding Algorithms Comparison

----

## Overview

*This project provides a robust framework for comparing and visualizing various pathfinding algorithms, such as Dijkstra, A Star, and BFS. Designed with scalability, maintainability, and visualization at its core, the project facilitates:*

- Performance analysis of algorithms based on execution time, path cost, steps, and path length.

- Interactive visualizations of graph traversal processes.

- Seamless integration with feature flag management for dynamic control of features.

- Automated testing suite for ensuring code quality and functionality.

---
## Features

#### 1. Algorithm Implementations

- Dijkstra's Algorithm: Computes the shortest path by iterating through the nodes with the smallest tentative distance.

- A* (A-Star Algorithm): Optimized for graph traversal with heuristics for better performance.

- Breadth-First Search (BFS): Explores all neighbors level by level, ideal for unweighted graphs.

#### 2. Visualization

- Real-time visual representation of graph traversal.

- Animated GIFs showing step-by-step pathfinding processes.

- Customizable node and edge styles.

#### 3. Metrics Comparison

- Compare algorithms on metrics like:

    - Execution Time (in seconds).
        
    - Path Cost (sum of edge weights).
        
    - Steps (number of iterations).
        
    - Path Length (number of edges in the path).
  

- Generate charts for visual comparisons.

#### 4. Feature Flags

*Integrated with Flagsmith to enable or disable functionalities dynamically, such as algorithm visualization and comparisons.*

#### 5. Testing

- Comprehensive test suite with:

    - Unit tests for individual modules.
    
    - Integration tests for pipeline validation.
    
    - Performance benchmarks for algorithms.

---
## Project Structure

````
Pathfinding-Algorithms-Comparison/
├── main.py  # Entry point of the application.
├── algorithms/
│   ├── __init__.py
│   ├── dijkstra.py
│   ├── a_star.py
│   └── bfs.py
├── core/
│   ├── __init__.py
│   ├── algorithm_comparator.py
│   ├── algorithm_context.py
│   ├── command.py
│   ├── decorators.py
│   ├── dependency_injector.py
│   ├── feature_flags.py
│   ├── graph_processor.py
│   ├── graph_styler.py
│   ├── graph_visualizer.py
│   └──  path_reconstructor.py
├── utils/
│   ├── __init__.py
│   └── graph_initializer.py
├── tests/
│   ├── test_a_star.py  
│   ├── test_bfs.py  
│   ├── test_dijkstra.py 
│   ├── test_dependency_injector.py
│   ├── test_graph_processor.py
│   ├── test_integration_pipeline.py
│   ├── test_path_reconstructor.py
│   ├── test_style_edge.py
│   ├── test_visual_regression.py
│   └── test_visualizer.py  
├── results/  # Output directory for visualizations and comparisons.
├── .flake8
├── requirements.txt
└── .github/
    └── workflows/
        └── python-tests-linting.yml
````

---
## Getting Started

#### Prerequisites

- Python 3.9+

- Virtual Environment (recommended)

- Libraries:

    - osmnx
    
    - matplotlib
    
    - pandas
    
    - pytest
    
    - flagsmith
    
    - Pillow

#### Install dependencies:

```pip install -r requirements.txt```

---

## Usage

1. Clone the repository:

````git clone https://github.com/yourusername/pathfinding-algorithms-comparison.git````

````cd pathfinding-algorithms-comparison````

2. Initialize the environment:

````python -m venv venv````

`````source venv/bin/activate  # On Windows: venv\Scripts\activate`````

3. Run the application:

```python main.py```

4. View generated results in the results/ directory.

---

## Visualization

#### GIF Generation

**To enable visualization:**

- Set the **enable-visualizer** feature flag using Flagsmith.

- Run the application and find animations in **results/animations/**.

---

Testing

*Run all tests using pytest:*

```pytest```

**Sample Tests**

- **test_a_star_execution**: Verifies that A* calculates paths correctly.

- **test_visualizer_capture_frame**: Ensures that frames are captured during visualization.

- **test_dependency_injection**: Validates correct behavior of the Dependency Injector.

---
## Contributions

**Contributions are welcome! To contribute:**

1. Fork the repository.

2. Create a new branch (feature/my-feature).

3. Commit your changes (git commit -m "Add feature").

4. Push to the branch (git push origin feature/my-feature).

5. Open a pull request.

---

## License

>This project is licensed under the **MIT License**. Feel free to use, modify, and distribute the software.

---

---

