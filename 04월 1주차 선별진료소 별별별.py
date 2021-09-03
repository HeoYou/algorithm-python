import sys

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, max(lst) * n
mid = 0

while right >= left:
    mid = (left + right) // 2
    print(left, right)
    total = 0
    for t in lst:
        total += mid // t
    if total >= n:
        right = mid - 1
    else:
        left = mid + 1

print(left)
