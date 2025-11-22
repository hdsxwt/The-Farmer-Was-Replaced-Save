def f():
	if can_harvest():
		pass
	if get_entity_type() == Entities.Dead_Pumpkin or get_entity_type() == None:
		plant(Entities.Pumpkin)
from for_all import for_all

for_all(f)