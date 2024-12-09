def create_maze():
	goto_position(0,0)
	harvest()
	plant_bush()
	while not can_harvest():
		do_a_flip()
	while get_entity_type() != Entities.Hedge and get_entity_type() != Entities.Treasure:
		if num_items(Items.Fertilizer) < 1:
			trade(Items.Fertilizer)
		use_item(Items.Fertilizer)

def solve_mazes():
	while(True):
		create_maze()
		solve_single_maze()
		harvest()

def solve_single_maze():
	direction_of_travel = 0
	while get_entity_type() != Entities.Treasure:
		direction_of_travel = (direction_of_travel - 1) % 4 
		while not move(DIRECTION_OF_TRAVEL()[direction_of_travel]):
			#if cant turn left then try turning straight, right, then back
			direction_of_travel = (direction_of_travel + 1) % 4 
	#harvest()
	return

def solve_many_mazes():
	create_maze()
	solve_single_maze()
	for i in range(300):
		if measure() == None:
			break
		destination_x, destination_y = measure()
		while get_entity_type() == Entities.Treasure:
			fertilize()
		find_maze_solution(destination_x, destination_y, [])
	harvest()
	return
		
def find_maze_solution(destination_x, destination_y, visited):
	if get_entity_type() == Entities.Treasure:
		return True
    visited.append((get_pos_x(), get_pos_y()))
    possible_paths = []
    if (get_pos_x(), get_pos_y()+1) not in visited:
        score = find_distance(get_pos_x(), get_pos_y()+1, destination_x, destination_y)
        insert_sorted((North, score), possible_paths)
    if (get_pos_x(), get_pos_y()-1) not in visited:
        score = find_distance(get_pos_x(), get_pos_y()-1, destination_x, destination_y)
        insert_sorted((South, score), possible_paths)     
	if (get_pos_x()-1, get_pos_y()) not in visited:
        score = find_distance(get_pos_x()-1, get_pos_y(), destination_x, destination_y)
        insert_sorted((West, score), possible_paths)
    if (get_pos_x()+1, get_pos_y()) not in visited:
        score = find_distance(get_pos_x()+1, get_pos_y(), destination_x, destination_y)
        insert_sorted((East, score), possible_paths)
    for i in range(len(possible_paths)):
        if move(possible_paths[i][0]):        
			if find_maze_solution(destination_x, destination_y, visited):
				return True
			move(OPPOSITE_DIRECTION()[possible_paths[i][0]])
    return False
    
def solve_mazes_until_value(value):
	single_maze_value = get_world_size() * get_world_size() * num_unlocked(Unlocks.Mazes)
	num_mazes_to_solve = value / single_maze_value
	farm_costs(get_cost(Items.Fertilizer), num_mazes_to_solve * 20)
	create_maze()
	solve_single_maze()
	if num_mazes_to_solve == 1:
		harvest()
		return
	if num_mazes_to_solve >= 300:
		num_mazes_to_solve = 299
	for i in range(num_mazes_to_solve):
		destination_x, destination_y = measure()
		while get_entity_type() == Entities.Treasure:
			if num_items(Items.Pumpkin) < get_cost(Items.Fertilizer)[Items.Pumpkin]:
				# we ran out of pumpkins so need to get more
				# it will get more when it tries to go back into the maze
				# and realizes it cant afford fertilizer
				harvest()
				return
			fertilize()
		find_maze_solution(destination_x, destination_y, [])
	harvest()
	return
	     
     