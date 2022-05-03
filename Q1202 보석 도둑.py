# import sys
# N, K = map(int, input().split())

# answer = 0
# jewelLst, bagLst= [], []
# for i in range(N):
#     jewelLst.append(list(map(int, sys.stdin.readline().split())))
# jewelLst = sorted(jewelLst, key = lambda x : x[1], reverse = True)

# for i in range(K):
#     bagLst.append(int(sys.stdin.readline()))
# bagLst = sorted(bagLst, reverse = True)

# for i in range(len(bagLst)):
#     for j in range(len(jewelLst)):
#         if bagLst[i] >= jewelLst[j][0]:
#             answer += jewelLst[j][1]
#             jewelLst.pop(j)
#             break


# print(answer)

# import heapq
# import sys


# N, K = map(int, input().split())

# answer = 0
# jewelLst, bagLst, tmp = [], [0] * K, []
# for _ in range(N):
#     heapq.heappush(jewelLst, list(map(int, sys.stdin.readline().split())))

# for i in range(K):
#     bagLst[i] = int(sys.stdin.readline())
# bagLst.sort()

# for i in bagLst:
#     while jewelLst and i >= jewelLst[0][0]:
#         heapq.heappush(tmp, -heapq.heappop(jewelLst)[1])
#     if tmp:
#         answer += -heapq.heappop(tmp)
#     elif not jewelLst:
#         break
    
# print(answer)

# import heapq
# import sys

# n, k = map(int, sys.stdin.readline().split(' '))
# jLst, bLst, tmp = [], [0] * k, []
# answer = 0
# for i in range(n):
#     heapq.heappush(jLst, list(map(int, sys.stdin.readline().split(' '))))
# for i in range(k):
#     bLst[i] = int(sys.stdin.readline())

# bLst.sort()

# for i in bLst:
#     while jLst and i >= jLst[0][0]:
#         heapq.heappush(tmp, -heapq.heappop(jLst)[1])
#     if tmp:
#         answer += -heapq.heappop(tmp)
#     elif not jLst:
#         break
# print(answer)


import sys
from heapq import heappop, heappush
N, K = map(int, input().split())
input = sys.stdin.readline
answer = 0
jewelLst, bagLst= [0] * N, [0] * K
for i in range(N):
    jewelLst[i] = list(map(int, sys.stdin.readline().split()))
jewelLst = sorted(jewelLst, reverse = True)

for i in range(K):
    bagLst[i] = int(sys.stdin.readline())
bagLst = sorted(bagLst)

q = []

for bag in bagLst:
    while jewelLst and bag >= jewelLst[-1][0]:
        heappush(q, -jewelLst.pop()[1])
    if q:
        answer -= heappop(q)

print(answer)