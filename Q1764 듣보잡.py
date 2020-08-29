import sys

n, m  = map(int, sys.stdin.readline().split())
nameLst = {}

for i in range(n):
    nameLst[sys.stdin.readline().strip()] = 0

nameLst2 = []
for i in range(m):
    name = sys.stdin.readline().strip()
    if name in nameLst:
        nameLst2.append(name)

print(len(nameLst2))
print('\n'.join(sorted(nameLst2)))

