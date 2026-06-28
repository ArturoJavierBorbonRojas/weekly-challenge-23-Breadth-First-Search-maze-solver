from collections import deque

# Week 23: Breadth-First Search (Maze Solver)
# Author: Ing. Arturo Javier Borbon Rojas

def print_maze(maze, path=None):
    """Helper function to print the maze visually."""
    maze_copy = [row[:] for row in maze]
    if path:
        # Mark the path with a special character, skipping start and end
        for r, c in path[1:-1]:
            maze_copy[r][c] = "*"
            
    for row in maze_copy:
        # 0 = Path (⬜), 1 = Wall (⬛), S = Start, E = End, * = Route
        line = ""
        for cell in row:
            if cell == 1: line += "⬛ "
            elif cell == 0: line += "⬜ "
            elif cell == "S": line += "🟢 "
            elif cell == "E": line += "🔴 "
            elif cell == "*": line += "⭐ "
        print(line)
    print("-" * 30)

def solve_maze_bfs(maze, start, end):
    print("🗺️ INITIAL MAZE:")
    print_maze(maze)
    
    rows = len(maze)
    cols = len(maze[0])
    
    # Queue for BFS: stores tuples of (current_position, path_taken_so_far)
    queue = deque([(start, [start])])
    
    # Set to keep track of visited cells to avoid infinite loops
    visited = set()
    visited.add(start)
    
    # Directions: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    steps = 0
    while queue:
        # FIFO: We pop from the left (the oldest element in the queue)
        current_pos, path = queue.popleft()
        steps += 1
        
        # If we reached the end, return the path
        if current_pos == end:
            print(f"✅ SUCCESS! Shortest path found in {steps} exploration steps.")
            print(f"📏 Path length: {len(path)} moves.")
            print("\n🗺️ SOLVED MAZE:")
            print_maze(maze, path)
            return path
            
        # Explore neighbors
        for dr, dc in directions:
            r, c = current_pos[0] + dr, current_pos[1] + dc
            
            # Check if the neighbor is inside bounds, is not a wall, and hasn't been visited
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] != 1 and (r, c) not in visited:
                visited.add((r, c))
                # Add the neighbor to the queue, and append it to our ongoing path
                queue.append(((r, c), path + [(r, c)]))
                
    print("❌ No valid path found.")
    return None

# --- Test Data ---
# 1 represents walls, 0 represents walkable paths
grid = [
    ["S", 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, "E"]
]

start_node = (0, 0)
end_node = (5, 5)

solve_maze_bfs(grid, start_node, end_node)