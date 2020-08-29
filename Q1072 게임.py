x, y = map(int, input().split())

rate = int((y / x) * 100)
answer = int((y / x) * 100)
count = 0
while rate == answer:
    count += 1
    x =+ 1
    y =+ 1
    answer = int((y / x) * 100)
    print(rate, answer)
print(count)