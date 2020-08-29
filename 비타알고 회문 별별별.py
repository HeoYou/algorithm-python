data = input()

n = int(input())

for i in range(n):
    s, e = map(int, input().split())
    if data[s - 1:e] == data[s - 1:e][::-1]:
        print(1)
    else:
        print(0)

