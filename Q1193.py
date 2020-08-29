n = int(input())

count = 0
sub = 1
while True:
    if n > sub:
        n -= sub
        sub += 1
    else: 
        break

if sub % 2 == 0:
    print(str(n) + "/" + str(sub + 1 - n))
else:
    print(str(sub + 1 - n) + "/" + str(n))
    