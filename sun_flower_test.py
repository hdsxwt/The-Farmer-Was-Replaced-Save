sim_items = {Items.Carrot:999999999, Items.Weird_Substance:9999999999}
speedup = 30
seed = 1
sim_globals = {}
res = []

sim_unlock = {}

for uk in Unlocks:
	sim_unlock[uk] = 20
	
# sim_unlock[Unlocks.Expand] = 5
# sim_unlock[Unlocks.Megafarm] = 2

res = simulate("sunflower", sim_unlock, sim_items, sim_globals, seed, speedup)
