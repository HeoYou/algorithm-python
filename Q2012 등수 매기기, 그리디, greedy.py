import sys

n = int(input())

lst = [0] * n
answer = 0

for i in range(n):
    lst[i] = int(sys.stdin.readline().strip())
lst.sort()

for i in range(n):
    answer += abs(i + 1 - lst[i])

print(answer)
