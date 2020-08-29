n = input()

if int(n) < 10:
    print(n)
else:
    result = 0
    sum = "9"
    for i in range(2, len(n)):
        sum += "0"
        result += int(sum) * i
    result += 9
    first = (int(n) - (10 ** (len(n) - 1))) + 1
    result += first * len(n)
print(result)

# result = 0
# for i in range(1, int(n) + 1):
#     result += len(str(i))
# print(result)


# 시간초과
# n = int(input())

# sum = 0

# for i in range(1, n + 1):
#     sum += len(str(i))
# print(sum)