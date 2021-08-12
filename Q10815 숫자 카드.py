_, dic = input(), {i: 1 for i in map(int, input().split(' '))}
input()
for i in list(map(int, input().split(' '))):
    print(dic.get(i, 0), end=' ')


# N = int(input())
# lst = sorted(list(map(int, input().split())))

# M = int(input())
# lst2 = list(map(int, input().split()))

# def BS(n):
#     left, mid, right = 0, N // 2, N - 1

#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] > n:
#             right = mid - 1
#         elif lst[mid] < n:
#             left = mid + 1
#         else:
#             return 1
#     return 0

# answer = [0] * M
# for i in range(M):
#     answer[i] = BS(lst2[i])

# print(' '.join(map(str, answer)))
