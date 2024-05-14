import networkx as nx
import matplotlib.pyplot as plt

# Sample CDP neighbor information (device: [neighbor1, neighbor2, ...])
cdp_neighbors = {
    "Switch1": ["Switch2", "Router1"],
    "Switch2": ["Switch1", "Router2"],
    "Router1": ["Switch1"],
    "Router2": ["Switch2"]
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes (devices)
for device in cdp_neighbors:
    G.add_node(device)

# Add edges (connections)
for device, neighbors in cdp_neighbors.items():
    for neighbor in neighbors:
        G.add_edge(device, neighbor)

# Draw the network diagram
pos = nx.spring_layout(G)  # Layout for the nodes
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Network Diagram")
plt.show()

