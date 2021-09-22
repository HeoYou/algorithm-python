# n = int(input())

# a, b = 0, 1
# while n >= 1:
#     b, a = a + b, b
#     n -= 1

# print(b)
def solution(n):
    a, b = 0, 1
    while n >= 1:
        b, a = a + b, b
        n -= 1
    return b % 1234567

print(solution(5))