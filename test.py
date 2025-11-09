sim_items = {Items.Carrot:999999999, Items.Weird_Substance:9999999999}
speedup = 1
seed = 1
sim_globals = {}
res = []

sim_unlock = {}

for uk in Unlocks:
	sim_unlock[uk] = 20
	
sim_unlock[Unlocks.Expand] = 5
sim_unlock[Unlocks.Megafarm] = 2

# modify
k = 5

for i in range(k):
	seed = i * i
	tmp = simulate("multi_template", sim_unlock, sim_items, sim_globals, seed, speedup)
	res.append(tmp)
	quick_print(tmp)

sum = 0
for i in range(k):
	sum += res[i]
print("ave" , sum / k)