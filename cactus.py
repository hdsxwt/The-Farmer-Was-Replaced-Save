from std import *

def run_cactus(target=None, data=None):
	clear()
	siz = get_world_size()
	def f():
		for j in range(siz):
			try_plant(Grounds.Soil, Entities.Cactus)
			move(East)
		for j in range(siz-1):
			move_to(0, i)
			for k in range(siz-j-1):
				if measure(East) < measure():
					swap(East)
				move(East)
	for i in range(siz):
		if not spawn_drone(f):
			f()
		move(North)
	
	while num_drones() != 1:
		pass

	move_to(0, 0)

	def g():
		for j in range(siz-1):
			move_to(i, 0)
			for k in range(siz-j-1):
				if measure(North) < measure():
					swap(North)
				move(North)
	for i in range(siz):
		if not spawn_drone(g):
			g()
		move(East)
	
	while num_drones() != 1:
		pass
	harvest()
				
if __name__ == "__main__":
	run_cactus()