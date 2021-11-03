from uninformed_graph_search import UninformedGraphSearch


if __name__ == '__main__':
    '''Conduct AI Search (Pathfinding) on a social network graph'''
    # Initialize a graph network
    goal = 150
    pathfinder = UninformedGraphSearch(goal=goal, source='facebook')

    # Find path from initial to goal states using uninformed search algorithms
    initial = 1
    bfs_path = pathfinder.breadth_first_search(initial=initial)
    dfs_path = pathfinder.depth_first_search(initial=initial)

    # Output discovered paths
    print("PATHFINDING SOLUTIONS from", initial, "to", goal,
          "\n\tBFS: {0}\n\tDFS: {1}".format(bfs_path, dfs_path))
