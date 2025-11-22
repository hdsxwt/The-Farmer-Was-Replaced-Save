from std import *

def run_carrot(target=None, data=None):
	def f():
		try_plant(Grounds.Soil, Entities.Carrot)
	move_to(0, 0)
	for_all(f)
	
if __name__ == "__main__":
	while True:
		run_carrot()

# 17.7k / min