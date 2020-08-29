s1 = input()
s2 = input()

lst = [0 for i in range(26)]

for i in s1:
    if i in s2:
        lst[ord(i) - ord('a')] = 1


print(sum(lst))