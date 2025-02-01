import heapq
import matplotlib.pyplot as plt
import networkx as nx

# --- Uniform Cost Search (UCS) ---
def ucs(graph, start, goal):
    frontier = []
    heapq.heappush(frontier, (0, start))  # (cost, node)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor, cost in graph.get(current, []):  # Ensure it handles missing nodes
            new_cost = current_cost + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost, neighbor))
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)


# --- Greedy Best-First Search (GBFS) ---
def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))
    came_from = {start: None}
    visited = set()

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        visited.add(current)

        for neighbor, _ in graph.get(current, []):  # Properly unpack tuple
            if neighbor not in visited and neighbor not in came_from:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor))
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)


# --- A* Search ---
def a_star_search(graph, start, goal, heuristic):
    frontier = []
    heapq.heappush(frontier, (heuristic[start], start))  # (f, node)
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor, cost in graph.get(current, []):  # Properly unpack tuple
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    return reconstruct_path(came_from, start, goal)


# --- Helper Function: Reconstruct Path ---
def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return None  # No path found

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path


# --- Graph and Heuristic for Example ---
graph = {
    'S': [('A', 2)],
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 1)],
    'C': [('G', 2)],
    'G': []
}

heuristic = {
    'S': 4,
    'A': 3,
    'B': 2,
    'C': 1,
    'G': 0
}

start = 'S'
goal = 'G'

# Running the search algorithms
ucs_path = ucs(graph, start, goal)
gbfs_path = greedy_best_first_search(graph, start, goal, heuristic)
a_star_path = a_star_search(graph, start, goal, heuristic)

print("UCS Path:", ucs_path)
print("GBFS Path:", gbfs_path)
print("A* Path:", a_star_path)

# --- Visualization of the Graph ---
def draw_graph(graph):
    G = nx.DiGraph()  # Use DiGraph for directed edges

    for node in graph:
        for neighbor, cost in graph[node]:
            G.add_edge(node, neighbor, weight=cost)

    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Graph Visualization")
    plt.show()

# Drawing the graph visualization
draw_graph(graph)
