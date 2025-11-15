def commonRet():
	return [0]
	# the position 0 is signal
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
	
	id = shared[0] + 1
	shared.append(id)
	shared[0] += 1
	while True:
		f(id, shared)

for i in range(max_drones()):
	if not spawn_drone(worker):
		worker()
	move(North)