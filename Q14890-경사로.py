import sys
input = sys.stdin.readline

def chk(lst):
	chkLst = [False] * N
	
	before = lst[0]
	for i in range(1, N):
		if before == lst[i]:
			before = lst[i]
			
		else:
			if abs(before - lst[i]) > 1:
				print(1)
				return False
			
			elif before > lst[i]:
				print("i", i)
				count = 0
				while count < L:
					count += 1
					if i + count >= N:
						print(2)
						return False
					elif lst[i + count] != before - 1:
						print(3)
						print(i, count)
						print(lst[i + count], lst[i])
						return False
						
				for j in range(L):
					chkLst[i + j + 1] = True
					
				
			
			if before < lst[i]:
				count = 0
				while count < L:
					count += 1
					if i - count < 0:
						print(4)
						return False
					elif lst[i - count] != lst[i] - 1:
						print(5)
						return False	
		print(chkLst)
	return True
		
		

N, L = map(int, input().split())

b = [list(map(int, input().split())) for i in range(N)]
answer = 0

# for l in b:
# 	if chk(l):
# 		print(l)		
# 		answer += 1
# print()
# for j in range(N):
# 	if chk([b[i][j] for i in range(N)]):
# 		print([b[i][j] for i in range(N)])
# 		answer += 1
chk([2, 2, 2, 1, 1, 1])
print(answer)		
# lstTmp = [b[i][0] for i in range(N)]

# print(lstTmp)
# chk(lstTmp)

# print(N, L)
# for i in b:
# 	print(i)
