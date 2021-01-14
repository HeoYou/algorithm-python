N = int(input())
lst = sorted(list(map(int, input().split())))

M = int(input())
lst2 = list(map(int, input().split()))

def BS(n):
    left, mid, right = 0, N // 2, N - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] > n:
            right = mid - 1
        elif lst[mid] < n:
            left = mid + 1
        else:
            return 1
    return 0

answer = []
for i in lst2:
    answer.append(BS(i))

print(' '.join(map(str, answer)))
