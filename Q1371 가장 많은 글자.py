import sys

lst = [0] * 26
s = sys.stdin.read()

for i in s:
    if i.islower():
        lst[ord(i) - 97] += 1

for i in range(26):
    if lst[i] == max(lst):
        print(chr(i + 97), end='')
