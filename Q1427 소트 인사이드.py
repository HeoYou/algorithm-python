N = input()

data = []

for i in N:
    data.append(i)
data.sort()
data.reverse()

for i in data:
    print(i, end='')
