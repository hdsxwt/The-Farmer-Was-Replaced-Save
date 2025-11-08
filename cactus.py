from std import *

def run_cactus(target=None, data=None):
	move_to(0, 0)
	siz = get_world_size()
	for i in range(siz):
		for j in range(siz):
			try_plant(Grounds.Soil, Entities.Cactus)
			mov(0, 1)
		mov(1, 0)
	for i in range(siz):
		for j in range(siz-1):
			move_to(i, 0)
			for k in range(siz-j):
				if measure(North) < measure():
					swap(North)
				mov(0, 1)
	for i in range(siz):
		for j in range(siz-1):
			move_to(0, i)
			for k in range(siz-j):
				if measure(East) < measure():
					swap(East)
				mov(1, 0)
	harvest()
				
if __name__ == "__main__":
	while True:
		run_cactus()