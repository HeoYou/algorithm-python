H, M = map(int, input().split())

time = int(input())

h = time // 60
m = time % 60

if M + m >= 60:
    H += 1
H = (H + h) % 24
M = (M + m) % 60

print(H, M)