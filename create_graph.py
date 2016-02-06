
import cost_distance
from graph import WeightedGraph

def create_graph(filename):

    graph = WeightedGraph()
    #Gives the first line command-line arguement

    with open(filename) as file:
        vert_dict = {}
        edge_dict = {}
	    for line in file: # Variable 'line' loops over each line in the file
            line = line.strip() # Remove trailing newline character
        # Process the line here
            lineinput = line.split(",")

            if lineinput[0] == 'V':
                latitude = int(float(lineinput[2]*100000))
			    longitude = int(float(lineinput[3]*100000))
			    graph.add_vertex(int(lineinput[1]))
                ver_dict[int(lineinput[1])] = (latitude, longitude)

		    elif lineinput[0] == 'E':
			    point1 = vert_dict[int(lineinput[1])]
			    point2 = vert_dict[int(lineinput[2])]
			    weight = cost_distance(point1,point2)

                graph.add_edge(lineinput[1],lineinput[2],weight)
                edge_dict[(point1,point2)] = lineinput[3]

    return graph,vert_dict
