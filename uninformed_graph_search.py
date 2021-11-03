import gzip
import networkx as nx

def path_from_predecessors(predecessors, last_node_visited):
    path = []
    node = last_node_visited
    while isinstance(node, int):
        path.append(node)
        node = predecessors[node]
    path.reverse()
    return path

def initialize_graph(source):
    G = nx.Graph()
    if source == 'facebook':
        network_csv = 'facebook_combined.txt.gz'
        file = gzip.open(network_csv, "rt")
        G = nx.read_edgelist(file, create_using=nx.Graph(), nodetype=int)
    elif source == 'local':
        G.add_node(1, name='Diego', age=15, gpa=4.2, over_21=False)  # For now, we can ignore node features/attributes
        G.add_node(2, name='Mary', age=15, gpa=4.1, over_21=False)
        G.add_node(3, name='Mica', age=16, gpa=3.8, over_21=False)
        G.add_node(4, name='Sofia', age=17, gpa=4.0, over_21=False)
        G.add_node(5, name='Vicente', age=19, gpa=3.5, over_21=False)
        G.add_node(6, name='Lucia', age=20, gpa=3.5, over_21=False)
        G.add_node(7, name='Marisol', age=21, gpa=3.8, over_21=True)
        G.add_node(8, name='Elliot', age=22, gpa=3.4, over_21=True)
        G.add_node(9, name='Amber', age=23, gpa=3.3, over_21=True)
        G.add_node(10, name='Faye', age=24, gpa=3.5, over_21=True)
        G.add_node(11, name='Ricardo', age=24, gpa=3.0, over_21=True)
        G.add_node(12, name='Kimberly', age=24, gpa=3.1, over_21=True)
        G.add_node(13, name='Max', age=25, gpa=3.1, over_21=True)
        G.add_node(14, name='Judith', age=26, gpa=2.6, over_21=True)
        G.add_node(15, name='Rommel', age=26, gpa=2.9, over_21=True)
        G.add_edges_from([(1, 2), (1, 4), (1, 3), (4, 3), (3, 5), (5,12), (6,12), (6,7), (6,8), (6,9), (6,10), (7,8),
                          (7,9), (7,11), (8,10), (8,11), (10,12), (11,14), (11,13), (12,13), (12,14), (13,15), (14,15)])
    else: print('Invalid source. Options are \'facebook\' or \'local\'.')
    return G


class UninformedGraphSearch:
    def __init__(self, goal, source='facebook'):
        self.goal = goal
        self.graph = initialize_graph(source)
        print(nx.info(self.graph), 'initialized.\n')

    def is_goal(self, node):
        return node == self.goal

    def get_neighbors(self, node):
        return self.graph[node]

    def breadth_first_search(self, initial):
        queue = [initial]
        visited = []
        predecessors = {initial: None}
        while queue:
            current_node = queue.pop(0)
            visited.append(current_node)
            if self.is_goal(current_node):
                break
            for neighbor in self.get_neighbors(node=current_node):
                if neighbor not in visited and neighbor not in queue:
                    predecessors[neighbor] = current_node
                    queue.append(neighbor)
        last_node_visited = visited[-1]
        if self.is_goal(last_node_visited):
            return path_from_predecessors(predecessors=predecessors, last_node_visited=last_node_visited)
        return "Goal not found."

    def depth_first_search(self, initial):
        stack = [initial]
        visited = []
        predecessors = {initial: None}
        while stack:
            current_node = stack.pop()
            visited.append(current_node)
            if self.is_goal(current_node):
                break
            for neighbor in self.get_neighbors(node=current_node):
                if neighbor not in visited and neighbor not in stack:
                    predecessors[neighbor] = current_node
                    stack.append(neighbor)
        last_node_visited = visited[-1]
        if self.is_goal(last_node_visited):
            return path_from_predecessors(predecessors=predecessors, last_node_visited=last_node_visited)
        return "Goal not found."