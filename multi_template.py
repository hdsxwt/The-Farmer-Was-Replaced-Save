def commonRet():
	return [[0, []]]
	# the position 0 is signal
clear()
drone = spawn_drone(commonRet)

def f(id, shared):
	quick_print(id)
	do_a_flip()
	do_a_flip()
	do_a_flip()

def worker():
	shared = wait_for(drone)
	
	id = shared[0][0]
	G = shared[0][1]
	G.append(1)
	shared.append(id)
	shared[0][0] += 1
	while True:
		f(G, shared)

for i in range(max_drones()):
	if not spawn_drone(worker):
		worker()
	move(North)