N, K = map(int, input().split())

graph = [[] for i in range(N + 1)]

indegree = [0] * (N + 1)
s = []
answer = []


for i in range(K):
	lst = list(map(int, input().split()))
	
	for j in range(1, lst[0]):
		graph[lst[j]].append(lst[j + 1])
		indegree[lst[j + 1]] += 1
		
for i in range(1, N + 1):
	if indegree[i] == 0:
		s.append(i)
		
while s:
	
	node = s.pop()
	answer.append(node)
	
	for i in graph[node]:
		indegree[i] -= 1
		if indegree[i] <= 0:
			s.append(i)

if len(answer) < N:
	print(0)
else:
	for i in answer:
		print(i)

	
		
