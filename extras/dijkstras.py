from heapq import *
from cost_distance import cost_distance



def dijkstras(start_vert, graph, vert_dict):
	reached = {}
	runners = []
	#initialize runners with the start value
	heappush(runners, (0, start_vert, start_vert))
	#print("start_vert: "+str(start_vert))

	#While there are still runners traveling between nodes
	while(runners):
		print("\nrunners: ", runners)

		#get the least cost runner
		run = heappop(runners)
		print("popped: ", run)
		cost = run[0]
		dest = run[1]
		source = run[2]
		#print("runners: ", run)
		#if there has already been a runner at the destion skip this runner
		if dest in reached:
			continue# this node has already been reached

		#in the reached dictionary, set the node that was reached and store the
		#start location and the cost it took to get there
		reached[dest] = (source, cost)

		print("neighbours_and_weights: ", graph.neighbours_and_weights(dest))
		for adjacent in graph.neighbours_and_weights(dest):
			#print("dest: ", vert_dict[dest])
			#print("adjacent: ", vert_dict[adjacent[0]])
			print("adjacent: ", adjacent)
			heappush(runners, (cost + cost_distance(vert_dict[adjacent[0]], vert_dict[dest]), adjacent[0], dest))
	print("reached: ", reached)
	return reached
