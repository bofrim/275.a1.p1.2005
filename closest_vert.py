def closest_vert(x1,y1,vert_dict):

	distance = 10000000

	for i in vert_dict:
		tempdistance = cost_distance(x1,vert_dict[i[0]],y1,vert_dict[i[1]])
		if tempdistance < distance:
			distance = tempdistance

	return distance
