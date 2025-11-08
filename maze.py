from std import *


vis = []
G = []
lst = []
dr = [North, South, East, West]
rdr = [South, North, West, East]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
n = get_world_size()

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
	while bot != top:
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
				return
def get_pos():
	return (get_pos_x(), get_pos_y())

def run_maze_mul(target=None, data=None):
	clear()
	till()
	plant(Entities.Bush)
	substance = get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)
	global n
	n = get_world_size()
	
	# set the time here
	max_n = 10
	if data != None:
		max_n = data
	for i in range(n):
		vis.append([])
		G.append([])
		lst.append([])
		for j in range(n):
			vis[i].append(False)
			G[i].append([])
			lst[i].append(None)
			for k in range(4):
				G[i][j].append(True)
	
	build(0, 0)
	for i in range(max_n):
		treasure = measure()
		bfs( treasure, get_pos() )
		while get_pos() != treasure:
			move(lst[get_pos_x()][get_pos_y()])
		if i != max_n - 1:
			use_item(Items.Weird_Substance, substance)
	harvest()
	
	

def run_maze(target=None, data=None):
	run_maze_mul(target, data)
	
				
if __name__ == "__main__":
	#set_execution_speed(1)
	#set_world_size(4)
	run_maze_mul()
	
# time:379.12s