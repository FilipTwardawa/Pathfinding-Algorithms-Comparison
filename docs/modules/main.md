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

# Modules Overview

This page provides an overview of all modules in the project. Click on a module to view its detailed API documentation.
