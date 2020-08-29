s = input()

lst = [0 for i in range(26)]

for i in s:
    lst[ord(i) - 97] += 1

print(' '.join(map(str, lst)))