N, M = map(int, input().split())
r, c, d = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(N)]

def back(x, y, d):
	if d == 0:
		x -= 1
	elif d == 1:
		y -= 1
	elif d == 2:
		x += 1
	elif d == 3:
		y += 1
	
	return x, y

def chk_clean(map_lst, x, y, d):
	if d == 0:
		if map_lst[x][y - 1] == 0:
			return True
	elif d == 1:
		if map_lst[x - 1][y] == 0:
			return True	
	elif d == 2:
		if map_lst[x][y + 1] == 0:
			return True	
	elif d == 3:
		if map_lst[x + 1][y] == 0:
			return True	
	return False
	
	
answer = 0

while True:
	# print(r, c)
	if lst[r][c] == 0:
		answer += 1
		lst[r][c] = 2
	
	back_flag = True
	for i in range(4):
		if chk_clean(lst, r, c, d):
			back_flag = False
			d = (d - 1) % 4
			if d == 0:
				r -= 1
			elif d == 1:
				c += 1
			elif d == 2:
				r += 1
			elif d == 3:
				c -= 1
			break
		d = (d - 1) % 4
	
	if back_flag:
		if d == 0:
			if lst[r - 1][c] == 1:
				break
		elif d == 1:
			if lst[r][c - 1] == 1:
				break
		elif d == 2:
			if lst[r + 1][c] == 1:
				break
		elif d == 3:
			if lst[r][c + 1] == 1:
				break
	r, c = back(r, c, d)

print(answer)
		
		
		
		
	
