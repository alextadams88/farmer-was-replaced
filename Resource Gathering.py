def farm_pumpkins(amount):
	farm_costs(get_cost(Items.Pumpkin_Seed), calc_needed_seeds(Items.Pumpkin_Seed, amount))
	while num_items(Items.Pumpkin) < amount:
		single_big_pumpkin()
	
def farm_treasure(amount):
	while num_items(Items.Gold) < amount:
		solve_mazes_until_value(amount - num_items(Items.Gold))

def farm_cactus(amount):
	farm_costs(get_cost(Items.Cactus_Seed), calc_needed_seeds(Items.Cactus_Seed, amount))
	while num_items(Items.Cactus) < amount:
		cactus_farm()

def farm_sunflowers(amount):
	farm_costs(get_cost(Items.Sunflower_Seed), calc_needed_seeds(Items.Sunflower_Seed, amount))
	while num_items(Items.Power) < amount:
		sunflower_farm()

def farm_dinosaurs(amount):
	farm_costs(get_cost(Items.Egg), calc_needed_seeds(Items.Egg, amount))
	while num_items(Items.Bones) < amount:
		dinosaur_farm()

def farm_wood(amount):
#	if num_unlocked(Unlocks.Polyculture) > 0:
#		while num_items(Items.Wood) < amount:
#			polyculture_farm(Items.Wood, amount)
	while num_items(Items.Wood) < amount:
		wood_farm()

def farm_carrots(amount):
#	if num_unlocked(Unlocks.Polyculture) > 0:
#		while num_items(Items.Carrot) < amount:
#			polyculture_farm(Items.Carrot, amount)
#	else:
		farm_costs(get_cost(Items.Carrot_Seed), calc_needed_seeds(Items.Carrot_Seed, amount))
		while num_items(Items.Carrot) < amount:
			carrot_farm()

def farm_hay(amount):
#	if num_unlocked(Unlocks.Polyculture) > 0:		
#		while num_items(Items.Hay) < amount:
#			polyculture_farm(Items.Hay, amount)
#	else:
		while num_items(Items.Hay) < amount:
			grass_farm()


def farm_resource(resource, amount):
	if resource == Items.Pumpkin:
		farm_pumpkins(amount)
	elif resource == Items.Gold:
		farm_treasure(amount)
	elif resource == Items.Cactus:
		farm_cactus(amount)
	elif resource == Items.Sunflower_Seed or resource == Items.Power:
		farm_sunflowers(amount)
	elif resource == Items.Bones or resource == Items.Egg:
		farm_dinosaurs(amount)
	elif resource == Items.Wood:
		farm_wood(amount)
	elif resource == Items.Carrot:
		farm_carrots(amount)
	elif resource == Items.Hay:
		farm_hay(amount)
	else:
		print("ERROR!!!")

#This function takes as input a seed type and the amount of the resurce I need
#I.e Items.Pumpkin_Seed and 100 indicating I need 100 pumpkins
#The function will return the amount of seeds I should buy.
def calc_needed_seeds(seed, num_needed):
	if seed == Items.Pumpkin_Seed:
		current_pumpkin_yield = get_world_size() * get_world_size() * get_world_size() * num_unlocked(Unlocks.Pumpkins)
		num_needed_pumpkins = num_needed // current_pumpkin_yield
		if num_needed % current_pumpkin_yield != 0 or num_needed_pumpkins == 0:
			num_needed_pumpkins = num_needed_pumpkins + 1
		seeds_per_pumpkin = get_world_size() * get_world_size()
		total_seeds_needed = seeds_per_pumpkin * num_needed_pumpkins
		total_seeds_needed = total_seeds_needed * 0.5 # pumpkins have 0.2 chance of dying, lets get 0.5 extra to cover bases
		return total_seeds_needed
	elif seed == Items.Sunflower_Seed:
		#sunflowers yield the sum from 1 to X of sqrt(X)
		# for example a 5x5 farm yields around 85 power (minus the power consumed while harvesting)
		# cannot calc this without numpy or a lot of fancy calc
		# so i will just estimate
		current_sunflower_yield = sunflower_farm_yield()
		num_farms_needed = num_needed // sunflower_farm_yield()
		if num_needed % current_sunflower_yield != 0 or num_farms_needed == 0:
			num_farms_needed = num_farms_needed + 1
		return get_world_size() * get_world_size() * num_farms_needed
	elif seed == Items.Cactus_Seed:
		cactus_farm_yield = get_world_size() ** 3 * num_unlocked(Unlocks.Cactus)
		num_farms_needed = num_needed // cactus_farm_yield
		if num_needed % cactus_farm_yield != 0 or num_farms_needed == 0:
			num_farms_needed = num_farms_needed + 1 
		return get_world_size() * get_world_size() * num_farms_needed
	elif seed == Items.Carrot_Seed:
		carrot_farm_yield = get_world_size() ** 2 * num_unlocked(Unlocks.Carrots) * 3
		num_farms_needed = num_needed // carrot_farm_yield
		if num_needed % carrot_farm_yield != 0 or num_farms_needed == 0:
			num_farms_needed = num_farms_needed + 1
		return get_world_size() * get_world_size() * num_farms_needed
	elif seed == Items.Egg:
		#TODO: This is wrong but I don't care
		return get_world_size() * get_world_size() 
	else:
		print("ERROR!!!! NO SEED FOUND")
		
	
#returns the approximate yield of a sunflower farm of the current world size.
def sunflower_farm_yield():
	world_size = get_world_size()
	yield = 0
	if world_size == 1:
		yield = 1
	elif world_size == 3:
		yield = 19
	elif world_size == 4:
		yield = 44
	elif world_size == 5:
		yield = 85
	elif world_size == 6:
		yield = 146
	elif world_size == 7:
		yield = 231
	elif world_size == 8:
		yield = 345
	elif world_size == 9:
		yield = 490
	elif world_size == 10:
		yield = 671
	else:
		print("ERROR!!! INVALID WORLD SIZE")
	return yield * num_unlocked(Unlocks.Sunflowers)
	
	