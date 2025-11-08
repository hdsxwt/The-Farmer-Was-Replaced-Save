from std import *

def run_carrot(target=None, data=None):
	move_to(0, 0)
	siz = get_world_size()
	for i in range(siz):
		for j in range(siz):
			try_plant(Grounds.Soil, Entities.Carrot)
			mov(0, 1)
		mov(1, 0)
	
if __name__ == "__main__":
	while True:
		run_carrot()

# 17.7k / min