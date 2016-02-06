def least_cost_path (graph, start, dest, cost):
	"""Find and return the least cost path in graph from start
	vertex to dest vertex. Efficiency: If E is the number of edges,
	the run-time is O( E log(E) ).

	Args:
	graph (Graph): The digraph defining the edges between the vertices.
	start: The vertex where the path starts. It is assumed that start is a vertex of graph.
	dest:  The vertex where the path ends. It is assumed that start is a vertex of graph.
	cost:  A function, taking the two vertices of an edge as parameters and
		returning the cost of the edge. For its interface, see the definition
		of cost_distance.

	Returns:
	list: A potentially empty list (if no path can be found) of the vertices in the
		graph. If there was a path, the first vertex is always start, the last is
		always dest in the list. Any two consecutive vertices correspond to some
		edge in graph.

		>>> graph = Graph({1,2,3,4,5,6}, [(1,2), (1,3), (1,6), (2,1), (2,3), (2,4),
		(3,1), (3,2), (3,4), (3,6), (4,2), (4,3), (4,5), (5,4), (5,6), (6,1), (6,3), (6,5)])

		>>> weights = {(1,2): 7, (1,3):9, (1,6):14, (2,1):7, (2,3):10, (2,4):15,
		(3,1):9, (3,2):10, (3,4):11, (3,6):2, (4,2):15, (4,3):11, (4,5):6, (5,4):6,
		(5,6):9, (6,1):14, (6,3):2, (6,5):9}

		>>> cost = lambda u, v: weights.get((u, v), float("inf"))
		>>> least_cost_path(graph, 1,5, cost) [1, 3, 6, 5] """
