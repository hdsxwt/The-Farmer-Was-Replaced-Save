def commonRet():
	return []
clear()
drone = spawn_drone(commonRet)
def worker():
	shared = wait_for(drone)
	while True:
		print(shared)

for i in range(max_drones() - 1):
	spawn_drone(worker)
	move(North)