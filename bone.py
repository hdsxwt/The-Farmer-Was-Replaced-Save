def run_bone():
	clear()
	change_hat(Hats.Dinosaur_Hat)
	siz = get_world_size()
	global cnt
	global x
	global y
	cnt = 0
	x, y = 0, 0
	def try_move(dir):
		if get_entity_type() == Entities.Apple:
			global cnt
			global x
			global y
			x, y = measure()
			cnt += 1
		return move(dir)
	while cnt < siz * (siz-3):
		quick_print(cnt, siz * (siz-3))
		try_move(North)
		k = (cnt - 2*siz + 2) / (siz - 1) / 2
		i = 0
		while i < k:
			for j in range(siz-2):
				try_move(North)
			try_move(East)
			for j in range(siz-2):
				try_move(South)
			try_move(East)
			i += 1
			k = (cnt - 2*siz + 2) / (siz - 1) / 2
		while get_pos_y() < y:
			try_move(North)
		while get_pos_x() < x:
			try_move(East)
		while get_pos_x() < siz-1:
			if get_pos_x() <= siz - 2 and not can_move(East):
				while get_pos_y() < siz-1:
					try_move(North)
			try_move(East)
		while get_pos_y() > 0:
			try_move(South)
		while get_pos_x() > 0:
			try_move(West)
	while True:
		k = siz / 2
		try_move(North)
		for i in range(k-1):
			for j in range(siz-2):
				try_move(North)
			try_move(East)
			for j in range(siz-2):
				try_move(South)
			try_move(East)
		for j in range(siz-2):
			try_move(North)
		try_move(East)
		for j in range(siz-2):
			try_move(South)
		try_move(South)
		for i in range(siz-1):
			try_move(West)
		if cnt == siz * siz - 1:
			break
	change_hat(Hats.Purple_Hat)

		

if __name__ == "__main__":
	set_world_size(16)
	run_bone()