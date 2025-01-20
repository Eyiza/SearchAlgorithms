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
    An example is this:
    Imagine you're lost in a forest, trying to find the tallest watchtower you can see on the horizon.
    You would walk toward the direction where the tower seems closest, hoping that each step brings you nearer to your goal.
    This is similar to how the greedy search algorithm works. It always selects the path which appears to be the best at that moment.
    The heuristic in this case is the visible distance to the watchtower.

"""
from visualize import visualize_graph, run_animation_in_thread # Import the visualize_graph_as_tree function from the visualize.py file
# Import the Node class from the node.py file
from node import Node, reconstruct_path
    

def greedy_best_first_search(start, goal, graph, heuristics):
    # Priority queue to hold nodes to explore, sorted by heuristic value
    priority_queue = []
    # Push the start node to the priority queue
    heapq.heappush(priority_queue, Node(start, heuristic=heuristics[start]))

    # Visited set to avoid revisiting nodes. We use the set data structure to store unique elements.
    visited = set()
    search_process = [] # List to store the search process for visualization

    # While there's possible nodes to visit
    while priority_queue:
        current_node = heapq.heappop(priority_queue) # Pop and return the smallest item from the heap
        current_state = current_node.state

        if current_state in visited:
            continue

        visited.add(current_state)
        search_process.append(current_state)
        # print(f"Visiting node: {current_state} with heuristic: {heuristics[current_state]}")


        # If the goal is reached, reconstruct the path
        if current_state == goal:
            path = reconstruct_path(current_node)
            run_animation_in_thread(graph, path, start, search_process, heuristics)
            return path

        # Explore neighbors in the graph i.e add the children of the node to the list of nodes to visit
        for neighbor in graph[current_state]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, Node(neighbor, current_node, heuristics[neighbor]))

    return None # If no path is found

# Example usage 
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F', 'G'],
#     'D': [],
#     'E': ['H'],
#     'F': [],
#     'G': [],
#     'H': []
# }
# heuristic = {
#     'A': 6, 'B': 3, 'C': 4, 'D': 3, 'E': 2, 'F': 6, 'G': 6, 'H': 0
# }

# Example usage 2 to demonstrate path is not optimal
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': ['H'],
    'G': [],
    'H': []
}
heuristic = {
    'A': 6, 'B': 3, 'C': 4, 'D': 6, 'E': 4, 'F': 2, 'G': 6, 'H': 0
}

start = 'A'
goal = 'H'

path = greedy_best_first_search(start, goal, graph, heuristic)
print(f"Path from {start} to {goal}: {path}")

# Visualize the graph and highlight the path
# visualize_graph(graph, path, start, heuristic)
