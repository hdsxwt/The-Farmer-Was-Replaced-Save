sim_items = {Items.Cactus:999999999, Items.Power: 99999}
speedup = 30
sim_globals = {}
res = []

sim_unlock = {}

for uk in Unlocks:
	sim_unlock[uk] = 20
	
# sim_unlock[Unlocks.Expand] = 5
# sim_unlock[Unlocks.Megafarm] = 2
while True:
	seed = random() * 65536 // 1
	quick_print(seed)
	res = simulate("bone", sim_unlock, sim_items, sim_globals, seed, speedup)
