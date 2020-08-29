import sys
lst = []

for i in range(int(input())):
    lst.append(sys.stdin.readline().strip())

lst = sorted(sorted(set(lst)), key=lambda x : len(x))

print("\n".join(lst))