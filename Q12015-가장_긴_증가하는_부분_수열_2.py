import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lis = []
answer = 0

for n in lst:
    if not lis:
        lis.append(n)
        continue
    
    if lis[-1] < n:
        lis.append(n)
    else:
        idx = bisect_left(lis, n)
        lis[idx] = n
        
print(len(lis))