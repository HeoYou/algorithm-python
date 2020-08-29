n = int(input())
sub = 1
count = 0
while n:
    if sub > n:
        sub = 1
    else:
        n -= sub
        sub += 1
        count += 1
print(count)