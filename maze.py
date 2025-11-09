from std import *

inf = 999999999
vis = []
G = []
lst = []
dis = []
dr = [North, South, East, West]
rdr = [South, North, West, East]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = get_world_size()
priority_queue = []

def build(x, y):
	vis[x][y] = True
	for k in range(4):
		if can_move(dr[k]):
			G[x][y][k] = True
			if not vis[ x+dx[k] ][ y+dy[k] ]:
				move(dr[k])
				build(x+dx[k], y+dy[k])
				move(rdr[k])
		else:
			G[x][y][k] = False

# change bfs to A*

def bfs(st, ed):
	bot = 0
	top = 0
	lis = []
	for i in range(n):
		for j in range(n):
			vis[i][j] = False
	top += 1
	lis.append( st )
	vis[st[0]][st[1]] = True
	
	cnt = 0
	
	while bot != top:
		cnt += 1
		ux, uy = lis[bot]
		bot += 1
		for k in range(4):
			if not G[ux][uy][k]:
				continue
			vx, vy = ux + dx[k], uy + dy[k]
			if vx < 0 or vx >= n or vy < 0 or vy >= n:
				continue
			if vis[vx][vy]:
				continue
			lst[vx][vy] = rdr[k]
			vis[vx][vy] = True
			top += 1
			lis.append( (vx, vy) )
			if (vx, vy) == ed:
				# quick_print("bfs", cnt)
				return
	# quick_print("bfs", cnt)
			

def A_star(st, ed):
	
	for i in range(n):
		for j in range(n):
			vis[i][j] = False
			# reset distance/grid cost
			dis[i][j] = inf

	def h(x, y):
		# Manhattan distance heuristic
		return abs(x - ed[0]) + abs(y - ed[1])

	sx, sy = st
	ex, ey = ed
	dis[sx][sy] = 0
	global priority_queue # (pos, dis) greater_queue
	priority_queue = []

	def push(x):
		pos, disp = x 
		l, r = 0,  len(priority_queue)
		while (l < r):
			mid = (l + r) // 2
			if priority_queue[mid][1] <= disp:
				l = mid + 1
			else:
				r = mid
		priority_queue.insert(l, x)

	push( (st, 0) )
	
	cnt = 0

	while len(priority_queue):
		cnt += 1
		u, disu = priority_queue[0]
		ux, uy = u
		priority_queue.remove(priority_queue[0])
		# skip if already processed
		if vis[ux][uy]:
			continue
		vis[ux][uy] = True
		if (ux, uy) == ed:
			# reached target; lst was filled on relaxations
			break
		for k in range(4):
			if not G[ux][uy][k]:
				continue
			vx, vy = ux + dx[k], uy + dy[k]
			if vx < 0 or vx >= n or vy < 0 or vy >= n:
				continue
			if vis[vx][vy]:
				continue
			disv = disu + 1
			if disv < dis[vx][vy]:
				dis[vx][vy] = disv
				# store direction to move from (vx,vy) back towards (ux,uy)
				lst[vx][vy] = rdr[k]
				push( ((vx, vy), disv + h(vx, vy)) )
	# no path found; leave lst as-is
	# quick_print("A*", cnt)
	return

def get_pos():
	return (get_pos_x(), get_pos_y())

def update():
	x, y = get_pos_x(), get_pos_y()
	for k in range(4):
		if can_move(dr[k]):
			G[x][y][k] = True

def run_maze_mul(target=None, data=None):
	clear()
	till()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	global n
	global vis
	global G
	global lst
	global dis
	vis = []
	G = []
	lst = []
	dis = []
	n = get_world_size()
	
	# set the time here
	max_n = 10
	if data != None:
		max_n = data
	for i in range(n):
		vis.append([])
		G.append([])
		dis.append([])
		lst.append([])
		for j in range(n):
			vis[i].append(False)
			G[i].append([])
			lst[i].append(None)
			dis[i].append(inf)
			for k in range(4):
				G[i][j].append(True)
	
	build(0, 0)
	for i in range(max_n):
		treasure = measure()

		#quick_print(i)
		bfs( treasure, get_pos() )
		# A_star( treasure, get_pos() )

		while get_pos() != treasure:
			move(lst[get_pos_x()][get_pos_y()])
			update()
		if i != max_n - 1:
			use_item(Items.Weird_Substance, substance)
	harvest()
	
	

def run_maze(target=None, data=None):
	run_maze_mul(target, data)
	
				
if __name__ == "__main__":
	#set_execution_speed(1)
	#set_world_size(5)
	run_maze_mul(None, 50)
	
# 10 times searching
# bfs no_updated: 419.28s
#		 updated: 419.34s
# A*  no_updated: 481.48s
#		 updated: 480.98s
	
# 200 times searching
# bfs no_updated: 5162.25s
#		 updated: 3336.66
# A*  no_updated: 6441.95s
#		 updated: 4183.9s