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



# from collections import deque
# import sys
# input = sys.stdin.readline


# n = int(input())

# q = deque()
# q.append([n])
# answer = []

# while q:
# 	node = q.popleft()
# 	v = node[0]
# 	if v == 1:
# 		answer = node
# 		break
	
# 	if v % 3 == 0:
# 		q.append([v // 3] + node)
# 	if node[0] % 2 == 0:
# 		q.append([v // 2] + node)
# 	q.append([v - 1] + node)
	
# print(len(answer) - 1)
# print(' '.join(map(str, answer[::-1])))


from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n = int(input())

q = deque()
q.append([n])
dp = [[] for i in range(n + 1)]
dp[n] = [n]


while q:
    node = q.pop()

    
    if node[-1] % 3 == 0:
        tmp = node[:] + [node[-1] // 3]
        if not dp[tmp[-1]] or len(dp[tmp[-1]]) > len(tmp):
            q.append(tmp)
            dp[tmp[-1]] = tmp
    if node[-1] % 2 == 0:
        tmp = node[:] + [node[-1] // 2]
        if not dp[tmp[-1]] or len(dp[tmp[-1]]) > len(tmp):
            q.append(tmp)
            dp[tmp[-1]] = tmp

    if node[-1] - 1 > 0:
        tmp = node[:] + [node[-1] - 1]
        if not dp[tmp[-1]] or len(dp[tmp[-1]]) > len(tmp):
            q.append(tmp)
            dp[tmp[-1]] = tmp
        
print(len(dp[1]) - 1)
print(*dp[1])