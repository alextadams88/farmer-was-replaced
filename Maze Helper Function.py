def find_distance(start_x, start_y, dest_x, dest_y):
	x_dist = abs(dest_x - start_x) ** 2
	y_dist = abs(dest_y - start_y) ** 2
	return x_dist + y_dist

def insert_sorted(new_path, paths):
	if len(paths) == 0:
		paths.append(new_path)
		return paths
	index = 0
	inserted = False
	while index < len(paths):
		if new_path[1] < paths[index][1]:
			paths.insert(index, new_path)
			inserted = True
			break
		index = index + 1
	if not inserted:
		paths.append(new_path)
	return paths