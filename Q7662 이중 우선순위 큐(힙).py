import sys
import heapq

input = sys.stdin.readline
temp = []
answer = []
visit = [True] * 1000001
for _ in range(int(input())):
    max_h, min_h = [], []

    for i in range(int(input())):
        c, x = map(str, input().split())
        if c == 'I':
            heapq.heappush(min_h, (int(x), i))
            heapq.heappush(max_h, (-int(x), i))
            visit[i] = False
        else:
            if len(min_h) and int(x) == -1:
                v, idx = heapq.heappop(min_h)
                print(visit)
                while visit[idx] and min_h:
                    visit[idx] = True
                    v, idx = heapq.heappop(min_h)
            elif len(max_h) and x:
                v, idx = heapq.heappop(max_h)
                while visit[idx] and max_h:
                    visit[idx] = True
                    v, idx = heapq.heappop(max_h)
        print(min_h, max_h)
