"""
    Depth First Search Algorithm is an algorithm that explores as deep as possible along each branch before backtracking.
    It uses a stack (LIFO) data structure to keep track of the nodes to visit.
    An example is this:
    If you are trying to find a book in a library, you would start at the first bookshelf and explore each book on that shelf before moving to the next shelf
    or if you're in a maze and and decide to take every left turn until you hit a dead end. You would explore each path as far as possible before turning back and trying a different path.
"""

from visualize import visualize_graph, run_animation_in_thread # Import the visualize_graph_as_tree function from the visualize.py file
from node import Node, reconstruct_path

def depth_first_search(start, goal, graph):
    # Stack to hold nodes to explore
    stack = []
    # Push the start node to the stack
    stack.append(Node(start))
    
    # Visited set to avoid revisiting nodes
    visited = set()
    search_process = [] # List to store the search process for visualization
    
    # While there's possible nodes to visit
    while stack:
        current_node = stack.pop() # Pop and return the rightmost item from the stack
        current_state = current_node.state
        
        if current_state in visited:
            continue
        
        visited.add(current_state)
        search_process.append(current_state)
        
        # If the goal is reached, reconstruct the path
        if current_state == goal:
            path = reconstruct_path(current_node)
            run_animation_in_thread(graph, path, start, search_process)
            return path
        
        # Explore neighbors in the graph i.e add the children of the node to the list of nodes to visit
        for neighbor in graph[current_state]:
            if neighbor not in visited and neighbor not in (node.state for node in stack):
                stack.append(Node(neighbor, current_node))
    
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
path = depth_first_search(start, goal, graph)
print(path) # Output: ['A', 'B', 'E', 'H']

# Visualize the graph and highlight the path
visualize_graph(graph, path, start)