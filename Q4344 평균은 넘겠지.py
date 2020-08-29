import sys

t = int(sys.stdin.readline())

for i in range(t):
    data = list(map(int, sys.stdin.readline().split()))
    avr = sum(data[1:]) / data[0]
    count = 0
    for j in data[1:]:
        if j > avr:
            count += 1
    print(str(format((count / data[0]) * 100, ".3f")) + "%")
