import sys

n = int(input())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
answer = 1

for i in range(n):
    if answer < lst[i]:
        break
    
    answer += lst[i]

print(answer)