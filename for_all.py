def for_all(f):
	def run():
		for i in range(get_world_size()):
			f()
			move(East)
	for i in range(get_world_size()):
		if not spawn_drone(run):
			run()
		move(North)