import sys
lst = [i + 1 for i in range(30)]
for i in range(28):
    lst.remove(int(sys.stdin.readline()))
print("\n".join(map(str, lst)))