from cost_distance import cost_distance

def closest_vert(x1,y1,vert_dict):

	#print(vert_dict)


	distance = 100000000

	for i in vert_dict:
		tempdistance = cost_distance((int(x1),vert_dict[i][0]),(int(y1),vert_dict[i][1]))
		if tempdistance < distance:
			distance = tempdistance
			close_vert = i


	#print(distance)

	return close_vert
