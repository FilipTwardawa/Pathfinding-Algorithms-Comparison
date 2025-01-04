"""
Module containing pathfinding algorithms: BFS, Dijkstra, and A*.
"""

import math
from time import time
import heapq
from typing import Tuple, List


class BFSAlgorithm:
    """Performs BFS on a graph."""

    def __init__(self, graph):
        self.graph = graph

    def execute(self, start: int, end: int) -> Tuple[List[int], float, float, int, int]:
        """Executes BFS from start to end."""
        time_start = time()
        self.graph.nodes[start]["distance"] = 0
        self.graph.nodes[start]["previous"] = None
        queue = [start]
        visited_count = 0

        while queue:
            current_node = queue.pop(0)
            if current_node == end:
                break

            for neighbor in self.graph.neighbors(current_node):
                if "visited" not in self.graph.nodes[neighbor]:
                    self.graph.nodes[neighbor]["visited"] = True
                    self.graph.nodes[neighbor]["previous"] = current_node
                    queue.append(neighbor)
                    visited_count += 1

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.graph.nodes[current].get("previous")

        path.reverse()
        time_end = time() - time_start
        return path, len(path) - 1, time_end, len(path), visited_count


class DijkstraAlgorithm:
    """Performs Dijkstra's algorithm on a graph."""

    def __init__(self, graph):
        self.graph = graph

    def execute(self, start: int, end: int) -> Tuple[List[int], float, float, int, int]:
        """Executes Dijkstra's algorithm from start to end."""
        time_start = time()
        distances = {node: float('inf') for node in self.graph.nodes}
        distances[start] = 0
        priority_queue = [(0, start)]
        visited_count = 0

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_node == end:
                break

            for neighbor, edge_data in self.graph[current_node].items():
                weight = edge_data.get("weight", 1)
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    self.graph.nodes[neighbor]["previous"] = current_node
                    visited_count += 1

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.graph.nodes[current].get("previous")

        path.reverse()
        time_end = time() - time_start
        return path, distances[end], time_end, len(path), visited_count


class AStarAlgorithm:
    """Performs A* algorithm on a graph."""

    def __init__(self, graph):
        self.graph = graph

    def heuristic(self, node1, node2):
        """Calculates heuristic based on straight-line distance."""
        x1, y1 = self.graph.nodes[node1]["x"], self.graph.nodes[node1]["y"]
        x2, y2 = self.graph.nodes[node2]["x"], self.graph.nodes[node2]["y"]
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def execute(self, start: int, end: int) -> Tuple[List[int], float, float, int, int]:
        """Executes A* algorithm from start to end."""
        time_start = time()
        open_set = [(0, start)]
        g_scores = {node: float('inf') for node in self.graph.nodes}
        g_scores[start] = 0
        f_scores = {node: float('inf') for node in self.graph.nodes}
        f_scores[start] = self.heuristic(start, end)
        visited_count = 0

        while open_set:
            _, current = heapq.heappop(open_set)
            if current == end:
                break

            for neighbor, edge_data in self.graph[current].items():
                weight = edge_data.get("weight", 1)
                tentative_g_score = g_scores[current] + weight
                if tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + self.heuristic(neighbor, end)
                    open_set.append((f_scores[neighbor], neighbor))
                    self.graph.nodes[neighbor]["previous"] = current
                    visited_count += 1

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = self.graph.nodes[current].get("previous")

        path.reverse()
        time_end = time() - time_start
        return path, g_scores[end], time_end, len(path), visited_count
