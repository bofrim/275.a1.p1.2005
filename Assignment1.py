from graph.py import WeightedGraph
import least_cost_path



import sys

graph = WeightedGraph()
vertex_list = []

filename = sys.argv[1] #Gives the first line command-line arguement

with open(filename) as file:
	for line in file: # Variable 'line' loops over each line in the file
		line = line.strip() # Remove trailing newline character
        # Process the line here
		lineinput = line.split(",")
		if lineinput[0] == 'V':
			graph.add_vertex(lineinput[1])
			vertex_list[lineinput[]] = 
		elif lineinput[0] == 'E':
			graph.add_edge(lineinput[1], lineinput[2])
