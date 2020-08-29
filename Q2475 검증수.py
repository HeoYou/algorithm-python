lst = [x ** 2 for x in map(int, input().split())]

print(sum(lst) % 10)