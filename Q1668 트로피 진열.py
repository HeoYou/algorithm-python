n = int(input())
left, right = 1, 1
lst = []

def solve(lst, num):
    top = 0
    count = 0
    for i in range(num):
        if lst[i] > top:
            top = lst[i]
            count += 1
    return count

for i in range(n):
    lst.append(int(input()))

print(solve(lst, n))
lst.reverse()
print(solve(lst, n))
