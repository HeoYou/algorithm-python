a, b = map(int, input().split())
answer = 1
while a < b:
    if b % 10 != 1 and b % 2 != 0:
        answer = -1
        break
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    answer += 1
print(answer if a == b else -1)