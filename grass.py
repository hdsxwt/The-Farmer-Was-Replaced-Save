from std import *

def run_grass(target=None, data=None):
	move_to(0, get_pos_y())
	def run():
		for j in range(get_world_size()):
			harvest()
			move(East)
	for i in range(max_drones()):
		if not spawn_drone(run):
			run()
		move(North)
	
				
if __name__ == "__main__":
	# set_execution_speed(1)
	while True:
		st = get_time()
		run_grass()
		quick_print(get_time() - st)
		
#ori 26.78s
#new 17.54s