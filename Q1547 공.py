# n = int(input())

# ball = 1

# for i in range(n):
#     a, b = map(int, input().split())
#     if a == ball:
#         ball = b
#     elif b == ball:
#         ball = a
# print(ball)

n = int(input())

l = [i for i in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    l[a], l[b] = l[b], l[a]

print(l.index(1))