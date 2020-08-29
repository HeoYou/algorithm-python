x = 1000 - int(input())
c = 0
co = [500, 100, 50, 10, 5, 1]
for i in co:
    c += x // i
    x = x % i
print(c)