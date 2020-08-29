import copy
M, N = map(int, input().split())
data = []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(N):
    data.append(list(map(int, input().split())))
copyData = copy.deepcopy(data)


while True:
    if data[:] == copyData[:]:
        for i in data:
            if 0


print(data)