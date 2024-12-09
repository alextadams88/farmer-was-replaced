# Inefficiency right now where I farm and harvest more than I need
# This is because the bulk of the harvesting is done during the plant() functions
# As it will harvest whatever's there before planting the next one
# Meaning that it will go ahead and plant the next one before checking if I have enough of what I need
# So I always farm a little bit extra, basically one extra round. This slows it down
# This also means that the cost calculations are wrong, so I end up getting enough resources for needed farms minus 1
# TODO: EFFICIENCY GAIN HERE!!! fix it so that either I stop doing the extra round, or I get enough resources for the extra round

# Current code does not take advantage of polycule farming.  
	
# Come up with a better solution for dinosaurs
	
# Double check that I'm handling the costs right in all scenarios:
# That i'm properly treating the return value as a dictionary and that
# I'm checking for the costs of the correct things (i.e. checking for cost of Carrot_Seed instead of Carrot)
	
#Some kind of weird delay in the early stages of bush farming
	
#Seems like I"m wasting time going back and forth between carrot farming and wood / hay farming to farm resources for seeds
#Could settle on how many seeds I need first total instead of re-checking it every loop - DONE (hopefully)
	
#add harvest() command after the do_a_flip() command in plant_carrot() - DONE
#sunflower code is too fast on smal farms and need to wait for the sunflowers to need fully grown before harvesting - DONE
#can probably bump up the watering constants. - DONE
	
# possibility of not enough resources being gathered by the first "farm_costs" calls in the resource gathering block
# because it only requests a specific amount, however the underlying call will attempt to plot the entire field
# which may be more than necessary
# so we may not get enough resource
	
#for some reason the third expand unlock doesn't seem to be happening??
#pumpkin code keeps harvesting the bottomr left corner # may have handled this
#need to substantially increase how much power I farm #added this
#OR do it more frequently
	
# it seems like some upgrades may be being skipped? maybe my code to get enough for the costs is wrong?
# or maybe its farming way more than it needs for resources?
# or farming for resources even when it already has the amount it needs 
# it looks like this is because of the way the stack works
# i have a function higher up the stack with a var called "amount"
	
#OH its because i'm farming way more than I need for pumpkin seeds
#because pumpkins give me the CUBED VALUE of the size of the pumpkin
#meaning a 5x5 pumpkin gives me 125 pumpkins but only requires 25 (+x) seeds
# but right now I'm making sure I Have enough resources for 125 pumpkin seeds
# thats why its taking FOREVER
# i'm also not taking into consideration the idea that there is a multiplier based on how much I've unlocked
# ok I think i handled this
	
#code to calc needed carrot seeds is wrong #FIXED
#carrot yield should be multiplied by 3 
# as it seems a single carrot tile actually gives 3 carrots
# who would have known
	
#Watering is not working because i have > 1 instead of >= 1 on the Unlocks.Watering in water_soil() function #DONE
#Polyculture code should move left move right insetad of doign a flip
#Polyculture code gets stuck waiting on trees to grow A LOT, i should probably make sure I have enough pumpkins in reserve to buy fertilizer before I enter polyculture
#fertilizer costs 10 pumpkins tho thats kind of a lot
# now i will not enter polyculture without 2000 pumpkins
#maybe I can just skip over the ones that are still growing if they are trees # made it so that if its a tree it skips otherwise it spins
	
#remove the do_a_flip() on the plant_grass()
#i'm running out of water need to buy more bucket
#the polyculture farm just takes way too long generally, when im farming for a specific item, it only loses me time instead of saves me time. i should turn that off
#unless i can find a way to take advantage of it while still mostly having a core farm but maybe not
#think about this more. if i have a tile of Grass and it wants a companion of Carrots at another place, I lose that tile of grass, but I gain 10x of the Grass. 
	
#It seems my code skipped the dinosaur stuff
#It unlocked the dinos, but when I called unlock(Unlocks.Leaderboard), it did not start farming dinosaurs and instead just errored that I couldnt afford it
	
#temp removed polyculture stuff