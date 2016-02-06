def cost_distance (u, v):
    '''Computes and returns the straight-line distance between the two vertices
    u and v.

    Args:
    u, v: The ids for two vertices that are the start and
        end of a valid edge in the graph.

    Returns:
        numeric value: the distance between the two vertices.
'''


'''
Dijkstras pseudocode:

reached = {} (empty dictionary)
runners = { (time, v, v) }
while runners is not empty
   extract (time, goal, start) with minimum time from runners
   if goal in reached
      continue        (ignore this runner and restart the loop)
   reached[goal] = (start, time)
   for each succ in goal
      add runner (time + cost(goal, succ), succ, goal) to runners
         (this new runner will reach succ at the given time)
return reached
'''
