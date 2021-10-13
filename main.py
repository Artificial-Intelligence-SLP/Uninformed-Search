from uninformed_graph_search import UninformedGraphSearch
import networkx as nx

def graph_to_search():
    # Initialize a graph, this will be our social network
    G = nx.Graph()
    # Add nodes to populate graph. You can give each node as many additional features as you like.
    G.add_node(1, name='Lucia')
    G.add_node(2, name='Marisol')
    G.add_node(3, name='Elliot')
    G.add_node(4, name='Amber')
    G.add_node(5, name='Faye')
    # Add edges between nodes
    G.add_edges_from([(1,2), (1,4), (1,3), (4,3), (3,5)])
    return G

def print_graph_summary(graph):
    print("GRAPH SUMMARY",
          "\nThere are {0} nodes with {1} edges.".format(graph.number_of_nodes(), graph.number_of_edges()))


if __name__ == '__main__':  # Running this file in Pycharm automatically runs the code below, our 'main' function.
    '''Initialize graph to search'''
    network = graph_to_search()
    print_graph_summary(network)

    '''Find path from initial to goal states using uninformed search algorithms'''
    initial = 1
    goal = 5
    pathfinder = UninformedGraphSearch(search_space=network, initial=initial, goal=goal)

    '''Output Solutions'''
    print("\nPATHFINDING SOLUTIONS from", initial, "to", goal,
          "\n\tBFS: {0}\n\tDFS: {1}".format(pathfinder.bfs_path, pathfinder.dfs_path))