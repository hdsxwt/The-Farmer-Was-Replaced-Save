
def run_grass():
	clear()

	def worker():
		while True:
			harvest()
			move(East)

	for i in range(get_world_size()):
		if not spawn_drone(worker):
			worker()
		move(North)

if __name__ == "__main__":
	run_grass()