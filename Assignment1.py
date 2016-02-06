
import least_cost_path.py
import cost_distance.py
import sys


def main():
	filename = sys.argv[1]
	graph = create_graph(filename)

	userin = input().split()
	if userin[0] == 'R':
		startlat = userin[1]
		startlon = userin[2]
		destlat = userin[3]
		destlon = userin[4]

		closest_vert(startlat,startlon,destlat,destlon)













if __name__ == '__main__':
	main()
