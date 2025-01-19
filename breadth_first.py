"""
    Breadth First Search Algorithm is an algorithm used to traverse or search tree or graph data structures.
    It starts from the root node and explores all the nodes at the present depth before moving on to the nodes at the next depth level.
    It uses a queue data structure to keep track of the nodes to visit.
    An example is this: 
    If you are searching for a person in a family tree, you would start from the root node (the person at the top of the tree) and explore all the children of that person before moving on to the grandchildren
    or if you're trying to find a friend in a crowded stadium, you would check every row, one row at a time, ensuring you explore all the people on the first row before moving to the second row, then the third, and so on.
"""

from collections import deque # Import the deque class from the collections module
from visualize import visualize_graph # Import the visualize_graph_as_tree function from the visualize.py file
from node import Node, reconstruct_path

def breadth_first_search(start, goal, graph):
    # Queue to hold nodes to explore
    queue = deque()
    # Push the start node to the queue
    queue.append(Node(start))

    # Visited set to avoid revisiting nodes
    visited = set()

    # While there's possible nodes to visit
    while queue:
        current_node = queue.popleft() # Pop and return the leftmost item from the queue
        current_state = current_node.state

        if current_state in visited:
            continue

        # If the goal is reached, reconstruct the path
        if current_state == goal:
            return reconstruct_path(current_node)
        
        visited.add(current_state)

        # Explore neighbors in the graph i.e add the children of the node to the list of nodes to visit
        for neighbor in graph[current_state]:
            if neighbor not in visited and neighbor not in (node.state for node in queue):
                queue.append(Node(neighbor, current_node))

    return None # If no path is found

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

start = 'A'
goal = 'H'
path = breadth_first_search(start, goal, graph)
print(path) # Output: ['A', 'B', 'E', 'H']

# Visualize the graph as a tree
visualize_graph(graph, path, start) # Output: A -> B, C -> D, E, F, G -> H
