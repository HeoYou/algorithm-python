a, b, c =  map(int, input().split())

n = int(input())
price, battery = 0, 0
lst5, lst8 = [], []

for i in range(n):
    data = list(map(int, input().split()))
    if data[1] == 0:
        lst5.append(data[0])
    else:
        lst8.append(data[0])
lst5.sort()
lst8.sort()

if a >= len(lst5):
    price = price + sum(lst5)
    battery = battery + len(lst5)
    lst5 = []
else:
    price = price + sum(lst5[:a])
    battery = battery + a
    lst5 = lst5[a:]

if b >= len(lst8):
    price = price + sum(lst8)
    battery = battery + len(lst8)
    lst8 = []
else:
    price = price + sum(lst8[:b])
    battery = battery + b
    lst8 = lst8[b:]

lst = sorted(lst5 + lst8)

if c >= len(lst5) + len(lst8):
    battery = battery + len(lst5) + len(lst8)
    price = price + sum(lst5) + sum(lst8)
else:
    battery = battery + c
    price = price + sum(lst[:c])

print(battery, price)
