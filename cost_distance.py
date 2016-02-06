from math import sqrt

def cost_distance (u, v):
    '''Computes and returns the straight-line distance between the two vertices
    u and v.

    Args:
    u, v: The ids for two vertices that are the start and
        end of a valid edge in the graph.

    Returns:
        numeric value: the distance between the two vertices.
    '''

    delta_x = u[0] - v[0]
    delta_y = u[1] - v[1]

    distance = sqrt((delta_x**2)+(delta_y**2))

    return int(distance)
