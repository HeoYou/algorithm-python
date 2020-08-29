import sys

n = int(sys.stdin.readline())
dic = {}
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())

    if b[0] == "e":
        dic[a] = ""
    else:
        del dic[a]

print('\n'.join(sorted(dic.keys(), reverse=True)))