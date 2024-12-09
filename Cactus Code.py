def plant_cactus_farm():
	clear_farm()
	goto_position(0,0)
	for i in range(get_world_size()):
		goto_position(0,i)
		for j in range(get_world_size()):
			plant_cactus()
			move(East)

# Bubble Sort seems like the best solution
# because I can only swap cactus
# with their immediate neighbor.
def sort_cactus():
	#sort horizontal
#	goto_position(0,0)
	for k in range(get_world_size()):
		goto_position(0,k)
		bubble_sort(k, "row")

					
	#sort vertical
	#goto_position(0,0)
	for k in range(get_world_size()):
		goto_position(k,0)
		bubble_sort(k, "column")

		
def bubble_sort(pos, type):
	direction = North
	start_pos_x = pos
	start_pos_y = 0
	if type == "row":
		direction = East
		start_pos_x = 0
		start_pos_y = pos
	for i in range(get_world_size()):
		sorted = True
		for j in range(get_world_size()-i):
			if measure() > measure(direction):
				sorted = False
				swap(direction)
			move(direction)
		if sorted:
			return True
		goto_position(start_pos_x,start_pos_y)

def cactus_farm():
	farm_costs(get_cost(Items.Cactus_Seed), get_world_size() * get_world_size())
	plant_cactus_farm()
	sort_cactus()
	harvest()
	
				