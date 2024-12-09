def setup_mixed_farm():
	clear_farm()
	goto_position(0,0)
	for i in range(get_world_size()):
		plant(Entities.Tree)
		move(East)
		plant(Entities.Bush)
		move(North)
		i = i + 1
		plant(Entities.Tree)
		move(West)
		plant(Entities.Bush)
		move(North)
	goto_position(2,0)
	plant_carrot()
	move(East)
	plant_carrot()
	move(East)
	plant_carrot()
	move(East)
	plant_carrot()
	move(North)
	plant_carrot()
	move(West)
	plant_carrot()
	move(West)
	plant_carrot()
	move(West)
	plant_carrot()

def farm():
	setup_mixed_farm()
	while True:
		#plant_sunflowers
		plant_sunflowers()
		goto_position(get_world_size() - 1, get_world_size() - 1)
		for i in range(get_world_size()):
			move(North)
			for j in range(get_world_size()):
				move(East)
				if in_sunflower_zone():
					continue
				if get_entity_type() == Entities.Bush:
					if can_harvest():
						harvest()
						plant(Entities.Bush)
				elif get_entity_type() == Entities.Carrots:
					if can_harvest():
						harvest()
						plant_carrot()
				elif get_entity_type() == Entities.Tree:
					if can_harvest():
						harvest()
						plant(Entities.Tree)
				elif get_entity_type() == Entities.Pumpkin:
					if can_harvest():
						harvest()
				else:
					if can_harvest():
						harvest()
		harvest_sunflowers()