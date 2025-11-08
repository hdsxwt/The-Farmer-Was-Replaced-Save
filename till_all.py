from more_move import *
siz = get_world_size()
for i in range(siz):
	for j in range(siz):
		if get_ground_type() == Grounds.Grassland:
			till()
		mov(1, 0)
	mov(0, 1)