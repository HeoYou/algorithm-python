import sys
import heapq

lst = []
answer = []
for i in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    if num == 0:
        print(0 if not lst else heapq.heappop(lst)[1])
    else:
        heapq.heappush(lst, [num * num + num / 10, num])