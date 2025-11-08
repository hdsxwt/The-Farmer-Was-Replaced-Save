from std import *
clear()
while True:
	for x in range(3, 8, 4):
		for y in range(3, 8, 4):
			move_to(x, y)
			if get_ground_type() == Grounds.Grassland:
				till()
			plant(Entities.Carrot)
			while get_water() <= 0.8:
				use_item(Items.Water)
			tmp = get_companion()
			move_to(tmp[1][0], tmp[1][1])
			harvest()
			plant(tmp[0])
			move_to(x, y)
			if can_harvest():
				use_item(Items.Fertilizer)
				harvest()
				plant(Entities.Carrot)