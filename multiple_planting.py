from try_plant import *

def commonRet():
	return [[0, [], []]]
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
	real = shared[0][2]
	shared.append(get_world_size()-1)
	shared[0][0] += 1
	if (id == 1):
		for i in range(get_world_size()):
			G.append([])
			real.append([])
			for j in range(get_world_size()):
				G[i].append(None)
				real[i].append(Entities.Grass)
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
		return shared[l] == shared[id] or shared[l] == shared[id] - 1
	def check_r():
		r = id + 1
		if (r == get_world_size() + 1):
			return True
		if shared[r] == shared[id] + 1 or shared[r] + get_world_size() == shared[id] + 1:
			return True
		if shared[r] == shared[id] + 2 or shared[r] + get_world_size() == shared[id] + 2:
			return True
		return False
	lst_time = get_time()
	min_water = 0.5
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
		x, y = get_pos_x(), get_pos_y()
		def llegal():
			if G[x][y] != Entities.Tree:
				return True
			if x != 0 and real[x-1][y] == Entities.Tree:
				return False
			if x != get_world_size() - 1 and real[x+1][y] == Entities.Tree:
				return False
			if y != 0 and real[x][y-1] == Entities.Tree:
				return False
			if y != get_world_size() - 1 and real[x][y+1] == Entities.Tree:
				return False
			return True
		if (G[x][y] != None and llegal()):
			c_try_plant(G[x][y])
			real[x][y] = G[x][y]
		else:
			c_try_plant(Entities.Grass)
			real[x][y] = Entities.Grass
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