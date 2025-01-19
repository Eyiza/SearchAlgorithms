class Node:
    def __init__(self, state, parent=None, heuristic=0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic

    # Magic method that is used to define or implement the functionality of the less than operator "<"
    def __lt__(self, other): 
        return self.heuristic < other.heuristic

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
