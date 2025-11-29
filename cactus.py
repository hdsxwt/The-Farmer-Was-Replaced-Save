from std import *

def run_cactus(target=None, data=None):
	clear()
	siz = get_world_size()
	def edit_in_line():
		for j in range(siz):
			try_plant(Grounds.Soil, Entities.Cactus)
			move(East)
		move_to(1, i)
		l, r = 0, siz-1
		op = 1
		while l < r:
			if op == 1:
				while get_pos_x() < r-1:
					if measure(East) < measure():
						swap(East)
					if measure(West) > measure():
						swap(West)
					if measure(East) < measure():
						swap(East)
					move(East)
				r -= 2
			else:
				while get_pos_x() > l+1:
					if measure(East) < measure():
						swap(East)
					if measure(West) > measure():
						swap(West)
					if measure(East) < measure():
						swap(East)
					move(West)
				l += 2
			op = -op

	def edit_in_row():
		move_to(i, 1)
		l, r = 0, siz-1
		op = 1
		while l < r:
			if op == 1:
				while get_pos_y() < r-1:
					if measure(North) < measure():
						swap(North)
					if measure(South) > measure():
						swap(South)
					if measure(North) < measure():
						swap(North)
					move(North)
				r -= 2
			else:
				while get_pos_y() > l+1:
					if measure(North) < measure():
						swap(North)
					if measure(South) > measure():
						swap(South)
					if measure(North) < measure():
						swap(North)
					move(South)
				l += 2
			op = -op
	for i in range(siz):
		if not spawn_drone(edit_in_line):
			edit_in_line()
		move(North)
	
	while num_drones() != 1:
		pass

	move_to(0, 0)

	for i in range(siz):
		if not spawn_drone(edit_in_row):
			edit_in_row()
		move(East)
	
	while num_drones() != 1:
		pass
	harvest()
				
if __name__ == "__main__":
	while True:
		run_cactus()