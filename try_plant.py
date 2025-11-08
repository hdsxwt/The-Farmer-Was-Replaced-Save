from std import *

def try_plant(ground, entity):
	if can_harvest():
		harvest()
	if get_ground_type() != ground:
		till()
	if get_water() <= 0.2:
		use_item(Items.Water)
	#if entity != Entities.Pumpkin:
		#if get_pos_x() == 0:
			#if get_ground_type() != Grounds.Soil:
				#till()
			#return plant(Entities.Sunflower)
	return plant(entity)
	
def try_plant_(data):
	return try_plant(data[0], data[1])