def mov(x, y):
	if x > 0:
		while x:
			move(East)
			x-=1
	elif x < 0:
		while x:
			move(West)
			x+=1
	
	if y > 0:
		while y:
			move(North)
			y-=1
	elif y < 0:
		while y:
			move(South)
			y+=1
			
def move_to(x, y):
	siz = get_world_size()
	dx = (get_pos_x()-x)
	dy = (get_pos_y()-y)
	
	def calc(x):
		while abs(x) > abs(x+siz):
			x += siz
		while abs(x) > abs(x - siz):
			x -= siz
		return x
	
	dx = calc(dx)
	dy = calc(dy)
	mov(-dx, -dy)

if __name__ == "__main__":
	move_to(3, 1)
	