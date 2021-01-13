lst = [0] * int(input())
answer = 0

for i in range(len(lst)):
    lst[i] = int(input())

print(lst)

for i in range(len(lst) - 1, 0, -1):
    sub = 0
    if lst[i] <= lst[i - 1]:
        sub = lst[i - 1] - lst[i] + 1
        answer += sub
        lst[i - 1] -= sub
        
print(answer)




N = int(input())
answer = 0

lst = [int(input()) for _ in range(N)]

for i in range(N - 1, 0, -1):

    if lst[i] <= lst[i - 1]:
        answer = lst[i - 1] - lst[i] + 1
        lst[i - 1] = lst[i] - 1

print(answer)