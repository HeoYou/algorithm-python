# import sys

# n = int(input())
# lst = [0] * n
# for i in range(n):
#     lst[i] = int(sys.stdin.readline())
# lst.sort()
# sum = 0
# pos = 1
# while True:
#     if pos >= n - 1:
#         break
#     if lst[pos - 1] * lst[pos] > lst[pos] * lst[pos + 1]:
#         sum += lst[pos - 1] * lst[pos]
#         pos += 2
#     else:
        
#         pos += 1

# print(sum)


import sys
answer = 0
n = int(input())
left, right, one= [], [], []
for i in range(n):
    num = int(sys.stdin.readline())
    if num <= 0:
        left.append(num)
    elif num == 1:
        one.append(num)
    else:
        right.append(num)  
left.sort()
right.sort(reverse = True)

for i in range(0, len(left) - 1, 2):
    answer += left[i] * left[i + 1]
if len(left) % 2 == 1:
    answer += left[-1]
for i in range(0, len(right) - 1, 2):
    answer += right[i] * right[i + 1]
if len(right) % 2 == 1:
    answer += right[-1]

print(answer + sum(one))

# pos = 0
# while pos < len(left) - 1:
#     answer += left[pos] * left[pos + 1]
#     pos += 2
# if len(left) % 2 == 1:
#     answer += left[-1]
#     pos = 0

# while pos < len(right) - 1:
#     answer += right[pos] * right[pos + 1]
#     pos += 2
# if len(right) % 2 == 1:
#     answer += right[-1]