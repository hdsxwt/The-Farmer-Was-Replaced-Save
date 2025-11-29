from std import *

def try_plant(ground, entity):
	if can_harvest():
		harvest()
	if get_ground_type() != ground:
		till()
	# if get_water() <= 0.4:
	# 	use_item(Items.Water)
	#if entity != Entities.Pumpkin:
		#if get_pos_x() == 0:
			#if get_ground_type() != Grounds.Soil:
				#till()
			#return plant(Entities.Sunflower)
	return plant(entity)


def c_try_plant(data):
	if data == Entities.Grass:
		if get_ground_type() != Grounds.Grassland:
			till()
	else:
		if get_ground_type() != Grounds.Soil:
			till()
	plant(data)
	return None

if __name__ == "__main__":
	try_plant(Entities.Bush)