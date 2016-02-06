from least_cost_path import least_cost_path
from dijkstras import dijkstras
from create_graph import create_graph
from closest_vert import closest_vert
import sys
#R 5365386 -1133915 5364728 -11335891


def main():
	filename = sys.argv[1]
	graph,vert_dict = create_graph(filename)
	#print(vert_dict)
	userin = input().strip().split()
	if userin[0] == 'R':
		startlat = userin[1]
		startlon = userin[2]
		destlat = userin[3]
		destlon = userin[4]
		print("begin mayhem!!!")

		start = closest_vert(startlat,startlon,vert_dict)
		end = closest_vert(destlat,destlon,vert_dict)
		#print(graph._alist)
		#print("neighbors1: "+str(list(graph.neighbours_and_weights(start))))

		path = least_cost_path(graph, start, end, 0, vert_dict)

		print(path)

		print("great success")













if __name__ == '__main__':
	main()
