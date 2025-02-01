Project 2 - Search Algorithms (UCS, Greedy BFS, A*)

Overview
This project implements three search algorithms to find the shortest path in a weighted graph:

Uniform Cost Search (UCS)
Greedy Best-First Search (GBFS)
A Search*
The goal is to compare these algorithms and analyze their effectiveness in finding the optimal path.

1. UCS (Uniform Cost Search)
Explores the graph by expanding nodes with the lowest cumulative cost.
Guarantees the optimal path but may be slower than other algorithms.
2. GBFS (Greedy Best-First Search)
Uses a heuristic to prioritize nodes that seem closer to the goal.
Fast but does not guarantee the optimal path.
3. A Search*
Combines UCS and GBFS by considering both cost and heuristic.

Implementation Details
Graph 1 (UCS Implementation): Finding the optimal path from A to E in a weighted graph.
*Graph 2 (GBFS vs. A)**: Evaluating which search algorithm finds the optimal path in a heuristic-based environment.
Language Used: Python
Code Quality: Well-commented, structured, and formatted for readability.
Guarantees the optimal path while being more efficient than UCS.

Findings and Observations
UCS guarantees the optimal path but is slower.
GBFS is faster but may not find the optimal path.
A* is the most efficient and guarantees the optimal path.

Submission Details
The submission includes the following files:

Python Code Implementation: Scripts for UCS, GBFS, and A* search algorithms.
Graph Visualization Code (if included): A script to visualize the graph structure.
Explanation of Algorithm Behavior: A brief description of how each algorithm works.
Findings and Comparisons of Results: Observations on which algorithm finds the optimal path and why.