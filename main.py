from std import *

def main():
	siz = get_world_size()
	state = None
	while True:
		if min(num_items(Items.Hay)/2, num_items(Items.Wood)/3, num_items(Items.Carrot)) >= max(num_items(Items.Pumpkin), siz * siz * 3) :
			state = Items.Pumpkin
		else:
			state = Items.Carrot
			
		if state == Items.Carrot:
			if min(num_items(Items.Hay)/2, num_items(Items.Wood)/3 >= num_items(Items.Carrot)):
				state = Items.Carrot
			else:
				state = Items.Wood

		if state == Items.Wood:
			if num_items(Items.Hay)/2 >= num_items(Items.Wood)/3:
				state = Items.Wood
			else:
				state = Items.Hay
		
		if num_items(Items.Power) <= 1000:
			state = Items.Power
		
		if state == Items.Pumpkin:
			run_pumkin(Items.Weird_Substance)
		elif state == Items.Carrot:
			run_carrot()
		elif state == Items.Wood:
			run_wood()
		elif state == Items.Hay:
			run_grass()
		elif state == Items.Power:
			run_sunflower()
	
if __name__ == "__main__":
	main()