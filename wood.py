from std import *

def run_wood(target=None, data=None):
	def f():
		if ((get_pos_x() + get_pos_y()) % 2 == 0):
			try_plant(Grounds.Soil, Entities.Tree)
		else:
			try_plant(Grounds.Soil, Entities.Bush)
	move_to(0, 0)
	for_all(f)
				
if __name__ == "__main__":
	while True:
		run_wood()