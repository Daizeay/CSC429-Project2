# graph_visualization.py
import networkx as nx
import matplotlib.pyplot as plt

# Create graph object and add nodes/edges
G = nx.Graph()
G.add_edges_from([
    ('S', 'A', {'weight': 2}),
    ('A', 'B', {'weight': 1}),
    ('A', 'C', {'weight': 4}),
    ('B', 'C', {'weight': 1}),
    ('C', 'G', {'weight': 2}),
])

# Create a layout for the graph visualization
pos = nx.spring_layout(G)

# Draw the graph
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', edge_color='gray')

# Add edge weights
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the plot
plt.title("Graph Visualization")
plt.show()
