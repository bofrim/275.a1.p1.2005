from cost_distance import cost_distance

def closest_vert(x1,y1,vert_dict):

	#print(vert_dict)


	distance = 100000000

	arbitrary_vert = (int(x1),int(y1))
	for i in vert_dict:
		if tempdistance < distance:
			distance = tempdistance
			close_vert = i


	#print(distance)

	return close_vert
