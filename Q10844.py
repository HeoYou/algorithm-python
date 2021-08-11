n = int(input())

answer = 9

for i in range(1, n):
    answer = answer * 2 - i
print(answer // 1000000000)