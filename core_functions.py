def goto_position(x,y):
	current_x = get_pos_x()
	current_y = get_pos_y()
	if current_x != x:
		east_distance = 0
		west_distance = 0
		if current_x > x:
			west_distance = current_x - x
			east_distance = (x + get_world_size()) - current_x
		else:
			west_distance = (current_x + get_world_size()) - x
			east_distance = x - current_x
		if east_distance < west_distance:
			move_direction(east_distance, East)
		else:
			move_direction(west_distance, West)
	if current_y != y:
		north_distance = 0
		south_distance = 0
		if current_y > y:
			north_distance = (y + get_world_size()) - current_y
			south_distance = current_y - y
		else:
			north_distance = y - current_y
			south_distance = (current_y + get_world_size()) - y
		if north_distance < south_distance:
			move_direction(north_distance, North)
		else:
			move_direction(south_distance, South)

def move_direction(n, direction):
	for i in range(n):
		move(direction)
		
def plant_carrot():
	if get_entity_type() != Entities.Carrots or can_harvest():
		harvest()
	elif get_entity_type() == Entities.Carrots:
		while not can_harvest():
			move(East)
			move(West)
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if num_items(Items.Carrot_Seed) < 1:
		trade(Items.Carrot_Seed)
	plant(Entities.Carrots)
	water_soil()

def plant_tree():
	if get_entity_type() != Entities.Tree or can_harvest():
		harvest()
	if get_ground_type() != Grounds.Turf:
		till()
	plant(Entities.Tree)

def get_tanks(x):
	current_tanks = num_items(Items.Empty_Tank) + num_items(Items.Water_Tank)
	if x - current_tanks > 0:
		buy_water_tanks(x - current_tanks)
	
def buy_water_tanks(x):
	farm_costs(get_cost(Items.Empty_Tank), x)
	trade(Items.Empty_Tank, x)

def water_soil():
	if num_unlocked(Unlocks.Watering) >= 1:
		while get_water() < WATER_THRESHOLD() and num_items(Items.Water_Tank) > 0:
			use_item(Items.Water_Tank)

def plant_pumpkin():
	if get_entity_type() != Entities.Pumpkin:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if num_items(Items.Pumpkin_Seed) < 1:
		trade(Items.Pumpkin_Seed)
	plant(Entities.Pumpkin)
	water_soil()

def get_pumpkin_start():
	return get_world_size() - PUMPKIN_SIZE()

def get_sunflower_start():
	return get_world_size() - SUNFLOWERS_SIZE()

def plant_sunflower():
	if get_entity_type() != Entities.Sunflower:
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if num_items(Items.Sunflower_Seed) < 1:
		trade(Items.Sunflower_Seed)
	plant(Entities.Sunflower)
	water_soil()

def in_sunflower_zone():
	current_x = get_pos_x()
	current_y = get_pos_y()
	if current_x >= get_world_size() - SUNFLOWERS_SIZE() and current_y >= get_world_size() - SUNFLOWERS_SIZE():
		return True
	return False

def plant_grass():
	if get_entity_type() != Entities.Grass or can_harvest():
		harvest()
	elif get_entity_type() == Entities.Grass:
		while not can_harvest():
			do_a_flip()
	if get_ground_type() != Grounds.Turf:
		till()

def plant_bush():
	if get_entity_type() != Entities.Bush or can_harvest():
		harvest()
	elif get_entity_type() == Entities.Bush:
		return
		#while not can_harvest():
		#	do_a_flip()
	if get_ground_type() != Grounds.Turf:
		till()
	plant(Entities.Bush)
	
def plant_plant(my_plant):
	if my_plant == Entities.Grass:
		plant_grass()
	elif my_plant == Entities.Bush:
		plant_bush()
	elif my_plant == Entities.Carrots:
		plant_carrot()
	elif my_plant == Entities.Pumpkin:
		plant_pumpkin()
	elif my_plant == Entities.Sunflower:
		plant_sunflower()
	elif my_plant == Entities.Tree:
		plant_tree()

def fertilize():
	if num_items(Items.Fertilizer) < 1:
		trade(Items.Fertilizer)
	use_item(Items.Fertilizer)

def plant_cactus():
	if get_entity_type() != Entities.Cactus or can_harvest():
		harvest()
	if get_ground_type() != Grounds.Soil:
		till()
	if num_items(Items.Cactus_Seed) < 1:
		trade(Items.Cactus_Seed)
	plant(Entities.Cactus)

def plant_dinosaur():
	if get_entity_type() != Entities.Dinosaur or can_harvest():
		harvest()	
	if num_items(Items.Egg) < 1:
		trade(Items.Egg)
	use_item(Items.Egg)
	
def farm_costs(cost_dict, amount):
	for item in cost_dict:
		needed_num = cost_dict[item] * amount
		if num_items(item) < needed_num:
			farm_resource(item, needed_num)

def unlock_ability(ability):
	cost = get_cost(ability)
	if cost == None:
		return # It's already unlocked
	#Need to handle special case where it farms resources of one type for the unlock, then spends those resources on seeds before it can do the unlock
	#Resulting in not having enough resources for the unlock
	while not can_afford(cost):
		farm_costs(cost, 1)
	unlock(ability)

def can_afford(costs):
	for cost in costs:
		if num_items(cost) < costs[cost]:
			return False
	return True