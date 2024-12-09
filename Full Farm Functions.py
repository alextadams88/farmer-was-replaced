def big_pumpkin_farm():
	clear_farm()
	while True:
		single_big_pumpkin()

def single_big_pumpkin():
	farm_costs(get_cost(Items.Pumpkin_Seed), get_world_size() * get_world_size() * 2)
	# do double the cost because of the way pumpkins behave
	found_empty = True
	while found_empty:
		found_empty = False
		goto_position(0,0)
		for i in range(get_world_size()):
			for j in range(get_world_size()):
#				if get_entity_type() == Entities.Pumpkin and not can_harvest():
#					move(East)
#					move(West)
				if get_entity_type() != Entities.Pumpkin:
					found_empty = True
					plant_pumpkin()
				elif get_entity_type() == Entities.Pumpkin and not can_harvest():
					found_empty = True
				move(East)
			move(North)
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


def carrot_farm():
	farm_costs(get_cost(Items.Carrot_Seed), get_world_size() * get_world_size())
	goto_position(0,0)
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			plant_carrot()
			move(East)
		move(North)

#Done
def wood_farm():
	if num_unlocked(Unlocks.Trees) < 1:
		goto_position(0,0)
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				plant_bush()
				move(East)
			move(North)
	else:
		goto_position(0,0)
		col = 0
		while col < get_world_size():
			row = 0
			while row < get_world_size():
				if col % 2 == 0:
					if row % 2 == 0:
						plant_tree()
					else:
						plant_bush()
				else:
					if row % 2 == 0:
						plant_bush()
					else:
						plant_tree()
				row = row + 1
				move(East)
			col = col + 1
			goto_position(0,col)

#Done
def grass_farm():
	goto_position(0,0)
	for i in range(get_world_size()):
		if num_unlocked(Unlocks.Expand) < 1:
			while not can_harvest():
				move(East)
			harvest()
			return
		elif num_unlocked(Unlocks.Expand) < 2:
			if can_harvest():
				harvest()
			move(North)
		else:
			for j in range(get_world_size()):
				plant_grass()
				move(East)
			move(North)

#Done
def polyculture_farm(item, amount):
	farm_resource(Items.Pumpkin, 2000) # Get enough pumpkins for 200 fertilizer at least
	goto_position(0,0)
	plant_grass()
	while num_items(item) < amount:
		companion = get_companion()
		if companion == None:
			plant_grass()
			companion = get_companion()
		goto_position(companion[1], companion[2])
		if not can_harvest():
			if num_items(Items.Pumpkin) > get_cost(Items.Fertilizer)[Items.Pumpkin]:
				fertilize()
			else:
				if get_entity_type() == Entities.Tree:
					continue
				else:
					while not can_harvest():
						move(West)
						move(East)
			harvest()
		plant_plant(companion[0])

#Done
def sunflower_farm():
	farm_costs(get_cost(Items.Sunflower_Seed), get_world_size() * get_world_size())
	plant_sunflowers()
	harvest_sunflowers()