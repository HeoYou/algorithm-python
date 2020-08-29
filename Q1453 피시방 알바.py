seat = [0 for i in range(101)]
answer = 0
n = int(input())
cus = list(map(int, input().split()))
for i in cus:
    if seat[i] == 0:
        seat[i] = 1
    else:
        answer += 1


print(answer)