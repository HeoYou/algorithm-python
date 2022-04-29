import sys
from itertools import combinations


answer = 0
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

left = arr[:N//2]
right = arr[N//2:]

leftDic, rightDic = {}, {}

for i in range(1, len(left) + 1):
	for j in combinations(left, i):
		s = sum(j)
		if s == S:
			answer += 1
		if leftDic.get(s):
			leftDic[s] += 1
		else:
			leftDic[s] = 1
for i in range(1, len(right) + 1):
	for j in combinations(right, i):
		s = sum(j)
		if s == S:
			answer += 1
		if rightDic.get(s):
			rightDic[s] += 1
		else:
			rightDic[s] = 1
			
for k in leftDic:
	rv = S - k
	if rightDic.get(rv):
		answer += leftDic[k] * rightDic[rv]

print(answer)
