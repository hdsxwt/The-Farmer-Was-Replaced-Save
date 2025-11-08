from std import *

def run_wood(target=None, data=None):
	move_to(0, 0)
	siz = get_world_size()
	for i in range(siz):
		for j in range(siz):
			if ((get_pos_x() + get_pos_y()) % 2 == 0):
				try_plant(Grounds.Soil, Entities.Tree)
			else:
				try_plant(Grounds.Soil, Entities.Bush)
			mov(0, 1)
		mov(1, 0)
				
if __name__ == "__main__":
	while True:
		run_wood()