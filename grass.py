from std import *

def run_grass(target=None, data=None):
	move_to(0, 0)
	siz = get_world_size()
	cnt = 0
	while (cnt < siz * siz):
		if can_harvest():
			harvest()
			cnt+=1
		if get_ground_type() != Grounds.Grassland:
			till()
		mov(0, 1)
				
if __name__ == "__main__":
	while True:
		st = get_time()
		run_grass()
		quick_print(get_time() - st)
		
#ori 26.78s
#new 17.54s