import sys
input = sys.stdin.readline

lst = []
zero, one = 0, 0
n = int(input())

def check_paper(paper):
    max_v = max(map(max, paper))
    min_v = min(map(min, paper))
    if max_v == min_v:
        return True
    else:
        return False

def re(n, x, y):
    global zero, one
    if check_paper([i[y : y + n] for i in lst[x : x + n]]):
        if lst[x][y]:
            one += 1
        else:
            zero += 1
    else:
        re(n // 2, x, y)
        re(n // 2, x, y + n // 2)
        re(n // 2, x + n // 2, y)
        re(n // 2, x + n // 2, y + n // 2)
    

for i in range(n):
    lst.append(list(map(int, input().split())))

re(n, 0, 0)

print(zero)
print(one)






