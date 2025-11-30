hats = [Hats.Brown_Hat, Hats.Cactus_Hat, Hats.Carrot_Hat, Hats.Purple_Hat, Hats.Tree_Hat]

for i in hats:
	def f():
		change_hat(i)
		while True:
			move(East)
	spawn_drone(f)
	move(North)