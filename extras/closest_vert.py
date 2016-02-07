from cost_distance import cost_distance

def closest_vert(x1,y1,vert_dict):

	distance = 100000000
	arbitrary_vert = (int(x1),int(y1))
	for i in vert_dict:
		tempdistance = cost_distance(arbitrary_vert,vert_dict[i])
		if tempdistance < distance:
			distance = tempdistance
			close_vert = i

	return close_vert
