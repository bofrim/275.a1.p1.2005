from heapq import *
from math import sqrt
import sys
#R 5365386 -1133915 5364728 -11335891


#==========================================================================
#==========================================================================


from graph import*


#==========================================================================
#==========================================================================

def create_graph(filename):

    graph = WeightedGraph()

    with open(filename) as file:
        for line in file: # Variable 'line' loops over each line in the file
            line = line.strip() # Remove trailing newline character
        # Process the line here
            lineinput = line.split(",")

            if lineinput[0] == 'V':
                latitude = int(float(lineinput[2])*100000)
                longitude = int(float(lineinput[3])*100000)
                graph.add_vertex(int(lineinput[1]))
                graph.vert_dict[int(lineinput[1])] = (latitude, longitude)

            elif lineinput[0] == 'E':
                point1 = vert_dict[int(lineinput[1])]
                point2 = vert_dict[int(lineinput[2])]
                weight = cost_distance(point1,point2)

                graph.add_edge(int(lineinput[1]),int(lineinput[2]),weight)
                graph.edge_dict[lineinput[1],lineinput[2]] = lineinput[3]


    return graph

#==========================================================================
#==========================================================================

def dijkstras(start_vert, graph):
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
			#print("adjacent: ", graph.vert_dict[adjacent[0]])
			print("adjacent: ", adjacent)
			heappush(runners, (cost + cost_distance(graph.vert_dict[adjacent[0]], graph.vert_dict[dest]), adjacent[0], dest))
	print("reached: ", reached)
	return reached

#==========================================================================
#==========================================================================

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

#==========================================================================
#==========================================================================

def closest_vert(x1,y1,graph):

	distance = 100000000
	arbitrary_vert = (int(x1),int(y1))
	for i in graph.vert_dict:
		tempdistance = cost_distance(arbitrary_vert,graph.vert_dict[i])
		if tempdistance < distance:
			distance = tempdistance
			close_vert = i

	return close_vert

#==========================================================================
#==========================================================================

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
	reached = dijkstras(start, graph)
	path = []
	ID = dest
	print(reached)
	cost = reached[dest][1]
	print('ID: ', ID)
	print('Start:', start)
	while(ID != start):
		print(ID)
		path.append(ID)
		ID = reached[ID][0]

	return path

#==========================================================================
#==========================================================================


def main():
	filename = sys.argv[1]
	graph = create_graph(filename)
	print("Comunication started...")
	while(True):
		userin = input("Please enter the start and end coordinates: ").strip().split()
		if len(userin) == 5:
			if userin[0] == 'R':
				startlat = userin[1]
				startlon = userin[2]
				destlat = userin[3]
				destlon = userin[4]

				print("begin mayhem!!!")

				start = closest_vert(startlat,startlon,graph)
				end = closest_vert(destlat,destlon,graph)

				#print(graph._alist)
				#print("neighbors1: "+str(list(graph.neighbours_and_weights(start))))

				path = least_cost_path(graph, start, end, 0)

				print(path)

				print("great success")
		else: print("Invalid request.")


if __name__ == '__main__':
	main()
