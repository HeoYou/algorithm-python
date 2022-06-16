
def tumble_dice(d, dir):
	new_d = [0] * 6
	if dir == 1:
		new_d[0] = d[3]
		new_d[1] = d[5]
		new_d[2] = d[2]
		new_d[3] = d[1]
		new_d[4] = d[4]
		new_d[5] = d[0]
	elif dir == 2:
		new_d[0] = d[5]
		new_d[1] = d[3]
		new_d[2] = d[2]
		new_d[3] = d[0]
		new_d[4] = d[4]
		new_d[5] = d[1]
	elif dir == 3:
		new_d[0] = d[4]
		new_d[1] = d[2]
		new_d[2] = d[0]
		new_d[3] = d[3]
		new_d[4] = d[1]
		new_d[5] = d[5]
	elif dir == 4:
		new_d[0] = d[2]
		new_d[1] = d[4]
		new_d[2] = d[1]
		new_d[3] = d[3]
		new_d[4] = d[0]
		new_d[5] = d[5]
		
	return new_d



dice = [0] * 6
N, M, x, y, c = map(int, input().split())
nx, ny = 0, 0
lst = [list(map(int, input().split())) for i in range(N)]
com = list(map(int, input().split()))

for c in com:
	# print(c, dice, lst, x, y)
	if c == 1:
		nx, ny = x, y + 1
	elif c == 2:
		nx, ny = x, y - 1
	elif c == 3:
		nx, ny = x - 1, y
	elif c == 4:
		nx, ny = x + 1, y
		
	if not (0 <= nx < N and 0 <= ny < M):
		# print("continue")
		continue
	x, y = nx, ny
	dice = tumble_dice(dice, c)
	
	if lst[x][y] == 0:
		lst[x][y] = dice[0]
	else:
		dice[0] = lst[x][y]
		lst[x][y] = 0
	
	print(dice[1])

