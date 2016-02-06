from graph.py import WeightedGraph
import least_cost_path.py
import cost_distance.py
import sys

import sys

graph = WeightedGraph()

filename = sys.argv[1] #Gives the first line command-line arguement

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
			latitude = int(float(lineinput[1]*100000))
			longitude = int(float(lineinput[2]*100000))
			graph.add_edge(latitude, longitude)
			edge_dict[latitude,longitude] = lineinput[3]
