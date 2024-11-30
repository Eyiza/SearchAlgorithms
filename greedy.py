"""
    Greedy search algorithm is a best-first search algorithm that uses heuristics to find the best path.
    It is not optimal, but it is efficient. It uses a priority queue to store the nodes. 
    The node with the lowest heuristic value is expanded first. 
"""
import heapq 
"""
    heapq is a Python module that provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
    It allows for efficient insertion and extraction of the smallest element from a collection of elements.
    Heaps are usually used to implement priority queues, where the smallest (or largest) element is always at the root of the tree.
    For a min-heap, the smallest element is at the root i.e for every node, the value of its children is greater than or equal to the value of the node.
    For a max-heap, the largest element is at the root i.e for every node, the value of its children is less than or equal to the value of the node.
"""
import networkx as nx # NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
import matplotlib.pyplot as plt # Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.

class Node:
    def __init__(self, state, parent=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic

    # Magic method that is used to define or implement the functionality of the less than operator "<"
    def __lt__(self, other): 
        return self.heuristic < other.heuristic
    

def greedy_best_first_search(start, goal, graph, heuristics):
    # Priority queue to hold nodes to explore, sorted by heuristic value
    priority_queue = []
    # Push the start node to the priority queue
    heapq.heappush(priority_queue, Node(start, heuristic=heuristics[start]))

    # Visited set to avoid revisiting nodes. We use the set data structure to store unique elements.
    visited = set()

    while priority_queue:
        current_node = heapq.heappop(priority_queue) # Pop and return the smallest item from the heap
        current_state = current_node.state

        # If the goal is reached, reconstruct the path
        if current_state == goal:
            return reconstruct_path(current_node)
        
        visited.add(current_state)

        # Explore neighbors in the graph
        for neighbor in graph[current_state]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, Node(neighbor, current_node, heuristics[neighbor]))

    return None # If no path is found

def reconstruct_path(node):
    """
    Reconstruct the path from start to goal using parent pointers.
    
    :param node: Goal node
    :return: List representing the path from start to goal
    """
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    path.reverse() # Reverse to get path from start to goal
    return path

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

def visualize_graph_as_tree(graph_dict, path, root):
    """
    Visualize the graph as a binary tree and highlight the chosen path.
    
    :param graph_dict: Dictionary representing the graph
    :param path: List of nodes in the chosen path
    :param root: Root node of the tree
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

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color=node_colors, edge_color=edge_colors, node_size=1500, font_size=12)
    plt.title("Graph Visualization with Highlighted Path")
    plt.show()

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': [],
    'H': []
}
heuristic = {
    'A': 6, 'B': 4, 'C': 4, 'D': 3, 'E': 2, 'F': 6, 'G': 6, 'H': 0
}

start = 'A'
goal = 'H'

path = greedy_best_first_search(start, goal, graph, heuristic)
print(f"Path from {start} to {goal}: {path}")

# Visualize the graph and highlight the path
visualize_graph_as_tree(graph, path, start)