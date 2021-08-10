n, l = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))

left, right = 1, max(trees)
while left <= right:
    mid = (left + right) // 2
    total = 0
    for i in trees:
        if i > mid:
            total += i - mid
    if total >= l:
        left = mid + 1
    else:
        right = mid - 1
print(right)

