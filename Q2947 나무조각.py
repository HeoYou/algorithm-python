import sys
n = sys.stdin.readline().split()

for j in range(len(n)):
    for i in  range(1, len(n)):
        if n[i] < n[i - 1]:
            n[i], n[i - 1] = n[i - 1], n[i]
            print(' '.join(n))
