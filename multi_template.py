def commonRet():
	return [None]
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
	id = num_drones()-1
	shared.append(id)
	while True:
		f(id, shared)

for i in range(max_drones()-1):
	spawn_drone(worker)
	move(North)

shared = wait_for(drone)
id = num_drones()
shared.append(id)
while True:
	f(id, shared)