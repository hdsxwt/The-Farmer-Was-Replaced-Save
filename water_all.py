from more_move import *
siz = get_world_size()
for i in range(siz):
	for j in range(siz):
		use_item(Items.Water)
		mov(1, 0)
	mov(0, 1)