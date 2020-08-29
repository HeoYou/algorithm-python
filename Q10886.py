import sys
data = [0, 0]
for i in range(int(sys.stdin.readline())):
    data[int(sys.stdin.readline())] += 1
print("Junhee is not cute!" if data[0] > data[1] else "Junhee is cute!")
