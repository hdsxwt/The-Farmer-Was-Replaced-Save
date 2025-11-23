sim_items = {Items.Carrot:999999999, Items.Weird_Substance:9999999999, Items.Water:9000000}
speedup = 100
seed = random()
sim_globals = {}
res = []

sim_unlock = {}

for uk in Unlocks:
	sim_unlock[uk] = 20
	
# sim_unlock[Unlocks.Expand] = 5
# sim_unlock[Unlocks.Megafarm] = 2

res = simulate("wood", sim_unlock, sim_items, sim_globals, seed, speedup)
