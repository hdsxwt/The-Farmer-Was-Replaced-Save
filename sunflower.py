from std import *

# TODO rebuild
# 采用多线程计数排序重构

def run_sunflower(target=None, data=None):
	
	st = get_tick_count()
	
	move_to(0, 0)
	siz = get_world_size()
	cnt = 0
	lis = []
	for i in range(siz):
		for j in range(siz):
			if try_plant(Grounds.Soil, Entities.Sunflower):
				lis.append( (measure(), (get_pos_x(), get_pos_y()) ) )
				cnt += 1
			mov(0, 1)
		mov(1, 0)
	lis = insertion_sort_binary(lis)
	for tmp in lis:
		move_to(tmp[1][0], tmp[1][1])
		while not can_harvest():
			if get_water() <= 0.7:
				use_item(Items.Water)
		harvest()
		cnt -= 1
		if cnt <= 10:
			break
	
	quick_print(get_tick_count() - st)
				
if __name__ == "__main__":
	while True:
		run_sunflower()
		
#average 91000 tick