ticks = 400
for i in range(200):
	print("吃掉 ", i, " 颗苹果后的 ticks: ", ticks)
	ticks -= ticks * 0.03 // 1