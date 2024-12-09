def sunflower_farm_loop():
	clear_farm()
	while(True):
		plant_sunflowers()
		harvest_sunflowers()

def plant_sunflowers():
	goto_position(get_sunflower_start(), get_sunflower_start())
	for i in range(SUNFLOWERS_SIZE()):
		goto_position(get_sunflower_start(), get_sunflower_start() + i)
		for j in range(SUNFLOWERS_SIZE()):
			plant_sunflower()
			move(East)

def harvest_sunflowers():
	goto_position(get_sunflower_start(), get_sunflower_start())
	sunflower_order = []
	inserted = False
	for i in range(SUNFLOWERS_SIZE()):
		for j in range(SUNFLOWERS_SIZE()):
			inserted = False
			current_index = 0
			while not can_harvest(): #wait for sunflowers to fully grow
				move(East)
				move(West)
			my_position = (get_pos_x(), get_pos_y(), measure())
			while not inserted:
				if len(sunflower_order) < 1 or current_index >= len(sunflower_order):
					sunflower_order.append(my_position)
					inserted = True
				else:
					if measure() >= sunflower_order[current_index][2]:
						sunflower_order.insert(current_index, my_position)
						inserted = True
					else:
						current_index = current_index + 1
			move(East)
		goto_position(get_sunflower_start(), get_sunflower_start() + i + 1)
			
	#create list of positions
	#iterate through list
	while(len(sunflower_order) > 0):
		goto_position(sunflower_order[0][0], sunflower_order[0][1])
		harvest()
		sunflower_order.pop(0)