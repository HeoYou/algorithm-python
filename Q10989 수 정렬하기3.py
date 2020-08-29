import sys

lst = [0] * 10001

for i in range(int(sys.stdin.readline())):
    lst[int(sys.stdin.readline())] += 1
for i in range(10001):
    for j in range(lst[i]):
        print(i)