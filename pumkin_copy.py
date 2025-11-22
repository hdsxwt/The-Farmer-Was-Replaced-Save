from more_move import *

def run_pumkin(st_x, st_y):
	siz = 6
	def f(st_x, st_y):
		move_to(st_x, st_y)
		vec = []
		vis = []
		cnt = 0
		for x in range(st_x, st_x + siz//2):
			for y in range(st_y, st_y + siz):
				move_to(x, y)
				if can_harvest():
					harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				if plant(Entities.Pumpkin):
					vec.append((x, y))
					vis.append(False)
					cnt += 1
		
		while(cnt != 0):
			for p in range(len(vec)):
				if vis[p] == True:
					continue
				move_to(vec[p][0], vec[p][1])
				if cnt <= 6 and get_water() <= 0.8:
					use_item(Items.Water)
				if can_harvest():
					vis[p] = True
					cnt-=1
				elif get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
				else:
					plant(Entities.Pumpkin)
	def ff():
		f(st_x+siz//2, st_y)
	while True:
		drone = spawn_drone(ff)
		f(st_x, st_y)
		wait_for(drone)
		harvest()
			
if __name__ == "__main__":
	clear()
	for x in range(1, get_world_size()-6, 7):
		for y in range(1, get_world_size()-6, 7):
			def f():
				run_pumkin(x, y)
			if not spawn_drone(f):
				f()
				
# 780k / min