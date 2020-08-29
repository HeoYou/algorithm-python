A, B, C = map(int, input().split())

print(B - A - 1 if B - A > C - B else C - B - 1)