def worker():
	pcnt = 0
	cnt = 0
	deadcnt = 0
	lst_t = get_time()
	while True:
		cnt += 1
		if get_pos_x() == 0 and get_pos_y() == 0:
			pcnt += 1
			if pcnt == 1:
				quick_print(deadcnt/cnt)
				quick_print(get_time() - lst_t)
				cnt = 0
				deadcnt = 0
				pcnt = 0
				lst_t = get_time()
		
		if get_ground_type() == Grounds.Grassland:
			till()
		
		water_line = 0.30 # min 0.30
		while (not can_harvest()) and get_entity_type() != None:
			deadcnt += 30
			if get_water() <= water_line:
				use_item(Items.Water)
		if get_water() <= water_line:
			use_item(Items.Water)
		harvest()
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Bush)
		else:
			plant(Entities.Tree)
		move(East)

def run_wood(target=None, data=None):
	for i in range(get_world_size()):
		if not spawn_drone(worker):
			worker()
		move(North)

				
if __name__ == "__main__":
	while True:
		run_wood()