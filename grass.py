
def run_grass():
	def worker():
		while True:
			if get_ground_type() == Grounds.Soil:
				till()
			harvest()
			move(East)

	for i in range(get_world_size()):
		if not spawn_drone(worker):
			worker()
		move(North)

if __name__ == "__main__":
	run_grass()