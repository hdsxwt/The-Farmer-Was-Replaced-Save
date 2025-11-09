from std import *

def run_pumkin(target=None, data=None):
	siz = get_world_size()
	move_to(0, 0)
	vec = []
	vis = []
	cnt = 0
	siz = get_world_size()
	for i in range(siz):
		for j in range(siz):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			if plant(Entities.Pumpkin):
				vec.append((i ,j))
				vis.append(False)
				cnt += 1
			mov(0, 1)
		mov(1, 0)
	
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
	if target == Items.Weird_Substance:
		move_to(0, 0)
		for i in range(siz):
			for j in range(siz):
				if (i*2+j)%5==0:
					use_item(Items.Weird_Substance)
				mov(0, 1)
			mov(1, 0)
	harvest()
			
if __name__ == "__main__":
	while True:
		run_pumkin(Items.Weird_Substance)