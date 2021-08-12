import heapq
import sys
heap = []
for i in range(int(input())):
    num = int(sys.stdin.readline())
    if num == 0:
        print(0 if len(heap) == 0 else -heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)