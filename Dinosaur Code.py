def plant_dinosaur_farm():
	clear_farm()
	goto_position(0,0)
	for i in range(get_world_size()):
		goto_position(0,i)
		for j in range(get_world_size()):
			plant_dinosaur()
			move(East)

#0 bottom left
#1 bottom right
#2 top left
#3 top right
#TODO: this code sucks its not smart at all
def corral_dinos():
	#just keep doing this repeatedly see how it works
	for i in range(get_world_size()):
		goto_position(0,i)
		for j in range(get_world_size()):
			harvest()
			move(East)

def dinosaur_farm():
	farm_costs(get_cost(Items.Egg), get_world_size() * get_world_size())
	plant_dinosaur_farm()
	corral_dinos()			


			