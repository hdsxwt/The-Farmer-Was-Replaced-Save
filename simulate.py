sim_items = {Items.Wood:1, Items.Weird_Substance:9999999999}
speedup = 600
seed = 1
sim_globals = {}
res = []

# modify
k = 5

for i in range(k):
	seed = random() * 65536 // 1
	tmp = simulate("maze", Unlocks, sim_items, sim_globals, seed, speedup)
	res.append(tmp)
	print(tmp)

sum = 0
for i in range(k):
	sum += res[i]
print("ave" , sum / k)