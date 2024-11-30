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