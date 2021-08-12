n = int(input())
lst = list(map(int, input().split()))
m = int(input())
left, right = 1, max(lst)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for l in lst:
        total += min(mid, l)
    if total > m:
        right = mid - 1
    else:
        left = mid + 1
print(right)
