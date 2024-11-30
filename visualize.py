import networkx as nx # NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
import matplotlib.pyplot as plt # Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

def binary_tree_layout(graph, root):
    """
    Create a layout for the graph to resemble a binary tree.

    :param graph: networkx DiGraph
    :param root: Root node of the binary tree
    :return: Dictionary of positions for each node
    """
    def helper(node, depth=0, pos={}, x=0, spacing=1.5):
        # Position for current node
        pos[node] = (x, -depth)
        neighbors = list(graph.successors(node))
        if neighbors:
            if len(neighbors) > 1:
                # Spread children horizontally
                left_x = x - spacing / 2
                right_x = x + spacing / 2
                helper(neighbors[0], depth + 1, pos, left_x, spacing / 2)
                helper(neighbors[1], depth + 1, pos, right_x, spacing / 2)
            else:
                # Single child case
                helper(neighbors[0], depth + 1, pos, x, spacing / 2)
        return pos

    return helper(root)

def visualize_graph(graph_dict, path, root, heuristics={}):
    """
    Visualize the graph as a binary tree, highlight the chosen path, and display heuristic values.
    
    :param graph_dict: Dictionary representing the graph
    :param path: List of nodes in the chosen path
    :param root: Root node of the tree
    :param heuristics: Dictionary of heuristic values for each node
    """
    G = nx.DiGraph()

    # Add edges to the graph
    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Create a binary tree layout
    pos = binary_tree_layout(G, root)

    # Define node colors
    node_colors = []
    for node in G.nodes():
        if node in path:
            node_colors.append('lightgreen')  # Highlight nodes in the path
        else:
            node_colors.append('lightblue')

    # Define edge colors
    edge_colors = []
    for edge in G.edges():
        if edge[0] in path and edge[1] in path and path.index(edge[1]) == path.index(edge[0]) + 1:
            edge_colors.append('green')  # Highlight edges in the path
        else:
            edge_colors.append('black')

    # Draw the graph with nodes and edges
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=1500, font_size=12)

    if heuristics:
        # Add heuristic values beside each node
        heuristic_label_pos = {node: (x + 0.155, y) for node, (x, y) in pos.items()}  # Shift labels to the right
        heuristic_labels = {node: f"h={heuristics[node]}" for node in G.nodes()}
        nx.draw_networkx_labels(G, heuristic_label_pos, labels=heuristic_labels, font_size=8, font_color="black")

    plt.title("Graph Visualization")
    plt.show()