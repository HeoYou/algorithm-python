# import sys
# sys.setrecursionlimit(10**6)

# n = int(input())
# answer = []
# answerCnt = 10**6

# def dfs(answerLst):
# 	global answerCnt
# 	if len(answerLst) > answerCnt:
# 		return
	
# 	if answerLst[-1] == 1:
# 		answer.append(answerLst)
# 		answerCnt = len(answerLst)
		
# 	paramLst = answerLst[:]
# 	if answerLst[-1] % 3 == 0:
# 		dfs(paramLst + [answerLst[-1] // 3])
# 	if answerLst[-1] % 2 == 0:
# 		dfs(paramLst + [answerLst[-1] // 2])
# 	if answerLst[-1] - 1 >= 1:
# 		dfs(paramLst + [answerLst[-1] - 1])

# dfs([n])
# print(answerCnt - 1)
# print(' '.join(map(str, sorted(answer, key = lambda x: len(x))[0])))
from collections import deque
import sys
input = sys.stdin.readline


n = int(input())

q = deque()
q.append([n])
answer = []

while q:
	node = q.popleft()
	v = node[0]
	if v == 1:
		answer = node
		break
	
	if v % 3 == 0:
		q.append([v // 3] + node)
	if node[0] % 2 == 0:
		q.append([v // 2] + node)
	q.append([v - 1] + node)
	
print(len(answer) - 1)
print(' '.join(map(str, answer[::-1])))
