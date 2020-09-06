n = int(input())
pay = [0] * (n + 2)
time = [0] * (n + 2)
answer = 0

for i in range(n):
    time[i + 1], pay[i + 1]  = map(int, input().split())
print(pay)
for i in range(n, 0, -1):
    if i + time[i] > n + 1:
        pay[i] = pay[i + 1]
    else:
        pay[i] = max(pay[i + 1], pay[i] + pay[i + time[i]])

print(max(pay))