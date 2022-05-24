import heapq
import sys

input = sys.stdin.readline
idx = [False] * 1000001

for _ in range(int(input())):
	minh, maxh = [], []
	for i in range(int(input())):
		comm, v = map(str, input().split())
		v = int(v)
		
		if comm == 'I':
			idx[i] = True
			heapq.heappush(minh, (v, i))
			heapq.heappush(maxh, (-v, i))
		else:
			if len(minh) == 0:
				continue
			if v == 1:
				while maxh and not idx[maxh[0][1]]:
					heapq.heappop(maxh)
				if maxh:
					v, id = heapq.heappop(maxh)
					idx[id] = False
				
			else:
				while minh and not idx[minh[0][1]]:
					heapq.heappop(minh)
				if minh:
					v, id = heapq.heappop(minh)
					idx[id] = False
					
			while maxh and not idx[maxh[0][1]]:
				heapq.heappop(maxh)
			while minh and not idx[minh[0][1]]:
				heapq.heappop(minh)
			
	if len(minh) == 0:
		print("EMPTY")
	else:
		print(-maxh[0][0], minh[0][0])