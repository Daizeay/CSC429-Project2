from collections import deque

# Grid structure as described (1: passable, 0: blocked)
grid = [
    [1, 1, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

# BFS Implementation (Grid)
def bfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start, [start])])  # (position, path)
    
    while queue:
        (x, y), path = queue.popleft()
        
        if (x, y) == goal:
            return path
        
        if (x, y) not in visited:
            visited.add((x, y))
            # Explore neighbors (up, down, left, right)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in visited:
                    new_path = path + [(nx, ny)]
                    queue.append(((nx, ny), new_path))
    return None


# DFS Implementation (Grid)
def dfs_grid(grid, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    
    x, y = start
    visited.add((x, y))
    path.append((x, y))
    
    if (x, y) == goal:
        return path
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1 and (nx, ny) not in visited:
            result = dfs_grid(grid, (nx, ny), goal, visited, path)
            if result:
                return result
    
    path.pop()  # backtrack
    return None


# Main function to test the algorithms on a grid
if __name__ == "__main__":
    # Test BFS on the grid
    start_point = (0, 0)  # Start at the top-left corner
    end_point = (4, 4)  # Goal at the bottom-right corner
    bfs_grid_path = bfs_grid(grid, start_point, end_point)
    print("BFS Path from A to B:", bfs_grid_path)

    # Test DFS on the grid
    dfs_grid_path = dfs_grid(grid, start_point, end_point)
    print("DFS Path from A to B:", dfs_grid_path)
