H, M = map(int, input().split())


H = (H - (M < 45)) % 24
M = (M - 45) % 60

print(H, M)