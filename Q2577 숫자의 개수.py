a, b, c = int(input()),int(input()),int(input())
d = a * b * c
answer = [0] * 10
while d > 0:
    answer[d % 10] += 1
    d //= 10

print('\n'.join(map(str, answer)))