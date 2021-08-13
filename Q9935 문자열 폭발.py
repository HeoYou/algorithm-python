a = input()
b = input()
while a.count(b) > 0:
    a = a.replace(b, '')

print(a if a else 'FRULA')