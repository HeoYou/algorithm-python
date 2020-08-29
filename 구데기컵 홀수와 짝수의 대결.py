import sys

t = int(sys.stdin.readline())

for i in range(t):
    num = int(sys.stdin.readline())
    if num % 2 == 0:
        print("O")
    else:
        print("E")

        