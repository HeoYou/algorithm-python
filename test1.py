n =  int(input())

answer = []

while True:
    if n == 2:
        answer.append(1)
        break
    elif n == 3:
        answer.append(7)
        break
    elif n > 3:
        n -= 2
        answer.append(1)

for i in answer:
    print(i, end="")




# def num(n):
#     if n == 2:
#         arr.append(1)
#         return -1
#     elif n == 3:
#         arr.append(7)
#         return -1
#     elif n >= 3:
#         return num(n - 2)
#
# def fibonacci(num):
#     if num < 2:
#         return num
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
#
# print(num(n))
# print(arr)