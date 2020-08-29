import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data = sorted(sorted(data, key = lambda x : x[0]), key = lambda x : x[1])

et = data[0][1]
count = 1

for i in range(1, n):

    if data[i][0] >= et:

        count += 1
        et = data[i][1]

print(count)
