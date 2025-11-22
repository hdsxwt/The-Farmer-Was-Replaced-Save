from more_move import *

def run_pumkin(siz, st_x, st_y, target = None):
	move_to(st_x, st_y)
	vec = []
	vis = []
	cnt = 0
	for x in range(st_x, st_x + siz):
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
	if target == Items.Weird_Substance:
		move_to(st_x, st_y)
		for i in range(st_x, st_x + siz):
			for j in range(st_y, st_y + siz):
				move_to(i, j)
				if (i*2+j)%5==0:
					use_item(Items.Weird_Substance)
	harvest()
			
if __name__ == "__main__":
	clear()
	for x in range(1, get_world_size(), 7):
		for y in range(1, get_world_size(), 7):
			def f():
				run_pumkin(6, x, y)
			if not spawn_drone(f):
				f()