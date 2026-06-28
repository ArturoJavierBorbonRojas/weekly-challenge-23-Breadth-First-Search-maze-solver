# Weekly challenge 23: Graph Theory & Pathfinding (Breadth-First Search)

## Description
Welcome to Week 23! This week, I dove into Graph Theory to implement one of the most fundamental search algorithms in Computer Science: **Breadth-First Search (BFS)**. 

To make it interactive, I applied the algorithm to solve a 2D grid maze. Given a starting point and a destination, the algorithm navigates through open paths, avoids walls, and finds the absolute shortest route to the exit.

## How it works
While heuristic algorithms like A* (which I built in Week 14) try to guess the direction of the target, BFS takes a methodical approach. 
1. It uses a **Queue (FIFO - First In, First Out)** data structure.
2. It explores the maze layer by layer, expanding equally in all directions (like a water ripple).
3. By keeping track of a `visited` set, it prevents infinite loops.
4. Because it searches level by level, the moment BFS finds the target in an unweighted graph (like a simple grid), it is mathematically guaranteed to be the shortest possible path.

## Complexity Analysis
* **Time Complexity:** $O(V + E)$ - Where $V$ is the number of vertices (cells) and $E$ is the number of edges (connections between cells). In the worst-case scenario, the algorithm visits every cell exactly once.
* **Space Complexity:** $O(V)$ - The maximum amount of memory needed for the Queue and the Visited Set scales linearly with the size of the maze.

## Dependencies
* Python 3.14.3 (Standard Library: `collections.deque`)
