from std import *

set_world_size(5)
clear()

def commonRet():
	return [0]
	# the position 0 is signal
drone = spawn_drone(commonRet)

def worker(x, y):
	shared = wait_for(drone)
	move_to(x, y)
	while True:
		if shared[0] > 300:
			break
		if get_entity_type() == Entities.Treasure:
			if shared[0] == 300:
				harvest()
			else:
				substance = 5 * 2**(num_unlocked(Unlocks.Mazes) - 1)
				use_item(Items.Weird_Substance, substance)
				shared[0] += 1
	

for i in range(5):
	for j in range(5):
		def f():
			worker(i, j)
		spawn_drone(f)


till()
plant(Entities.Bush)
substance = 5 * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)