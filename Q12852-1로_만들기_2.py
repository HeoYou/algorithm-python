import sys
sys.setrecursionlimit(10**6)

n = int(input())
answer = []
answerCnt = 10**6

def dfs(answerLst):
	global answerCnt
	if len(answerLst) > answerCnt:
		return
	
	if answerLst[-1] == 1:
		answer.append(answerLst)
		answerCnt = len(answerLst)
		
	paramLst = answerLst[:]
	if answerLst[-1] % 3 == 0:
		dfs(paramLst + [answerLst[-1] // 3])
	if answerLst[-1] % 2 == 0:
		dfs(paramLst + [answerLst[-1] // 2])
	if answerLst[-1] - 1 >= 1:
		dfs(paramLst + [answerLst[-1] - 1])

dfs([n])
print(answerCnt - 1)
print(' '.join(map(str, sorted(answer, key = lambda x: len(x))[0])))
