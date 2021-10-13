# This function does not need to be a class method. So we put it outside of the class, but within the same file so
# the class can still use it. Recall that class methods are object methods. An 'UninformedGraphSearch' object really
# has no reason to call this function by itself.
def deduce_path(predecessors, last_node_visited):
    path = []
    # Using predecessors dict, populated during the search, step backward from goal to deduce final path
    node = last_node_visited
    while node:  # This line functions the same as 'while node != None:'
        path.append(node)
        node = predecessors[node]
    path.reverse()  # Path = [Goal ... Initial], so reverse to [Initial ... Goal]
    return path


class UninformedGraphSearch:
    def __init__(self, search_space, initial, goal):
        # Save class variables
        self.graph = search_space
        self.goal = goal

        # Call class methods
        self.bfs_path = self.breadth_first_search(initial)
        self.dfs_path = self.depth_first_search(initial)

    def is_goal(self, node):
        return node == self.goal

    def get_neighbors(self, node):
        return self.graph[node]

    def breadth_first_search(self, initial):
        queue = [initial]  # Use queue to organize neighbors to visit next
        visited = []  # Use this list to not revisit nodes
        predecessors = {initial: None}  # Use a dictionary to record a node's predecessor
        while queue:  # While queue is not empty
            # Dequeue and visit that node
            current_node = queue.pop(0)
            visited.append(current_node)
            if self.is_goal(current_node):
                break   # If the node is the goal, exit the search (aka while loop)
            # Enqueue all neighbors of 'current_node' if they are unvisited & not already in the queue
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in visited and neighbor not in queue:
                    predecessors[neighbor] = current_node   # Add {neighbor:current_node} as a new element in 'predecessors'
                    queue.append(neighbor)  # Enqueue each valid neighbor of 'current_node'
        # End of while
        if self.is_goal(visited[-1]):  # Was the last node visited the goal? Tip: Index -1 points to the last element
            return deduce_path(predecessors=predecessors, last_node_visited=visited[-1])
        else:
            return "Goal not found."
    # End of method

    def depth_first_search(self, initial):
        stack = [initial]
        visited = []
        predecessors = {initial: None}
        while stack:  # While stack is not empty
            current_node = stack.pop()
            visited.append(current_node)
            if self.is_goal(current_node):
                break
            # Push all neighbors of that node if they are unvisited & not already in the stack
            for neighbor in self.get_neighbors(current_node):
                if neighbor not in visited and neighbor not in stack:
                    predecessors[neighbor] = current_node
                    stack.append(neighbor)
        # End of while
        if self.is_goal(visited[-1]):  # Was the last node visited the goal?
            return deduce_path(predecessors=predecessors, last_node_visited=visited[-1])
        else:
            return "Goal not found."
    # End of method

# End of class