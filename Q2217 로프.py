import sys

In = sys.stdin.readline

n = int(In())
rope = []
answer = 0
for i in range(n):
    rope.append(int(In()))

rope.sort()

for i in range(n):
    answer = max(answer, rope[i] * (n - i))

print(answer)