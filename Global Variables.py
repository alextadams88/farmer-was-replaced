def WATER_THRESHOLD():
	total_buckets = num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)
	if total_buckets < 20:
		return 0
	if total_buckets >= 20 and total_buckets < 50:
		return 0.2
	if total_buckets >= 50 and total_buckets < 100:
		return 0.35
	if total_buckets >= 100 and total_buckets < 500:
		return 0.5
	if total_buckets >= 500 and total_buckets < 1000:
		return 0.6
	if total_buckets >= 1000 and total_buckets < 5000:
		return 0.85
	if total_buckets >= 5000:
		return 1
	#return 0.75 #water soil if it is less wet than this value

def PUMPKIN_SIZE():
	return 2 # X by X size of pumpkin in top right corner

def SUNFLOWERS_SIZE():
	#return 3 # X by X size of sunflower farm in top right corner
	return get_world_size()
	
def DIRECTION_OF_TRAVEL():
	return {0:West, 1:North, 2:East, 3:South}
	
def OPPOSITE_DIRECTION():
	return {North:South, South:North, West:East, East:West}

	