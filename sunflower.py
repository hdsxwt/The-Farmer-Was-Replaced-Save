from std import *

# signal [7, 15]

siz_x = 4
siz_y = 8

def main():
	def commonRet():
		return [[0, 0]]
		# the position [0][0] is signal
		# the position [0][1] is cnt
	clear()
	drone = spawn_drone(commonRet)

	def f(id, shared):
		print(id)
		do_a_flip()
		do_a_flip()
		do_a_flip()
		print(shared)

	def worker():
		shared = wait_for(drone)
		G = {}
		for i in range(7, 16):
			G[i] = []
		id = shared[0][0]
		shared.append(id)
		shared[0][0] += 1
		id_x = id % (get_world_size() / siz_x)
		id_y = id // (get_world_size() / siz_x)
		st_x = id_x * siz_x
		st_y = id_y * siz_y
		if id == 0:
			while shared[0][0] < max_drones():
				pass
			shared[0][0] = -1
			shared[0][1] = 0
		# BUG
		while shared[0][0] != -1:
			pass

		# init

		move_to(st_x, st_y)

		for x in range(st_x, st_x + siz_x):
			for y in range(st_y, st_y + siz_y):
				move_to(x, y)
				try_plant(Entities.Sunflower)
				G[measure()].append((x, y))
		shared[0][1] += 1

		if id == 0:
			while shared[0][1] < num_drones():
				pass
			shared[0][0] = -2
		while shared[0][0] != -2:
			pass
		do_a_flip()
		if id == 0:
			print(shared)
		# TODO: harvest
		while True:
			pass

	for i in range(max_drones()):
		if not spawn_drone(worker):
			worker()
		move(North)

if __name__ == "__main__":
	set_execution_speed(10)
	main()