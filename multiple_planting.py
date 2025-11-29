from try_plant import *

def commonRet():
	return [[0, []]]
	# the position 0 is signal
move_to(0, 0)
drone = spawn_drone(commonRet)

def f(id, shared):
	quick_print(id)
	do_a_flip()
	do_a_flip()
	do_a_flip()

def worker():
	shared = wait_for(drone)
	
	id = shared[0][0] + 1 # start from 1
	G = shared[0][1]
	shared.append(get_world_size()-1)
	shared[0][0] += 1
	if (id == 1):
		for i in range(get_world_size()):
			G.append([])
			for j in range(get_world_size()):
				G[i].append(None)
		while (num_drones() < max_drones()):
			pass
		for i in range(500):
			pass
		shared[0][0] = -1
	
	while shared[0][0] != -1:
		pass
	def check_l():
		l = id - 1
		if l == 0:
			return True
		# quick_print(shared[l], shared[id]) # test
		return shared[l] == shared[id]
	def check_r():
		r = id + 1
		if (r == get_world_size() + 1):
			return True
		return shared[r] == shared[id] + 1 or shared[r] + get_world_size() == shared[id] + 1
	lst_time = get_time()
	min_water = 0.8
	while True:
		while (not check_l() or not check_r()):
			if get_water() <= min_water:
				use_item(Items.Water)
			pass
		while not can_harvest():
			if get_entity_type() == None:
				break
			use_item(Items.Fertilizer)
		harvest()
		if (G[get_pos_x()][get_pos_y()] != None):
			c_try_plant(G[get_pos_x()][get_pos_y()])
		else:
			c_try_plant(Entities.Carrot)
		plant_type, (x, y) = get_companion()
		G[x][y] = plant_type
		shared[id] = (shared[id] + 1) % get_world_size()
		move(North)
		if id == 1 and get_pos_y() == 0:
			quick_print(get_time() - lst_time)
			lst_time = get_time()

def main():
	for i in range(max_drones()):
		if not spawn_drone(worker):
			worker()
		move(East)

if __name__ == "__main__":
	# set_execution_speed(10)
	main()