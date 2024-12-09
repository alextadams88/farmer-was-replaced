def big_pumpkin():
	clear_farm()
	while True:
		found_empty = False
		goto_position(0,0)
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_entity_type() != Entities.Pumpkin:
					found_empty = True
					plant_pumpkin()
				move(East)
			move(North)
		if not found_empty:
			harvest()
		
def clear_farm():
	goto_position(0,0)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			harvest()
			if get_ground_type() == Grounds.Soil:
				till()
			move(East)
		move(North)

def companion_farm():
	clear_farm()
	goto_position(0,0)
	harvest()
	plant_grass()
	while(True):
		companion = get_companion()
		goto_position(companion[1], companion[2])
		if not can_harvest():
			fertilize()
			harvest()
		plant_plant(companion[0])

def sunflower_farm():
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
		