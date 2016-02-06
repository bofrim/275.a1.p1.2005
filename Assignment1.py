
import least_cost_path.py
import cost_distance.py
import sys


def main():
	filename = sys.argv[1]
	graph,vert_dict = create_graph(filename)

	userin = input().split()
	if userin[0] == 'R':
		startlat = userin[1]
		startlon = userin[2]
		destlat = userin[3]
		destlon = userin[4]

		start = closest_vert(startlat,startlon,vert_dict)
		end = closest_vert(destlat,destlon,vert_dict)

		print("great success")













if __name__ == '__main__':
	main()
