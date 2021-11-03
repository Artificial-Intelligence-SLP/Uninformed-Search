from uninformed_graph_search import UninformedGraphSearch
from linear_regression import LinearRegression


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


    '''Conduct AI Learning (Linear Regression) on a life expectancy data set
    # Train a linear regression model from network dataframe
    independent_var = ' BMI '
    dependent_var = 'Life expectancy '
    lr_model = LinearRegression(source='WHO', dependent=dependent_var, independent=independent_var)
    intercept, slope = lr_model.b[0], lr_model.b[1]

    # lr_model.display_plotted_data(x_label='Age (yr)', y_label='GPA')
    # parameters = lr_model.gradient_descent()
    # lr_model.plot_arbitrary_line(intercept=parameters[0], slope=parameters[1])

    # Output learned parameters
    print("MODEL PARAMETERS",
          "\n\tIntercept: {0}\n\tSlope: {1}".format(intercept, slope))
    '''