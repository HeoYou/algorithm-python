from collections import deque

def solution(key, lock):
    answer = True

    key = lstExtend(key)

    for _ in range(4):
        lock = rotate_90(lock)

        if chk(key, lock):
            return True

    return False


def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

def chk(k, l):
    kn = len(k)
    ln = len(l)

    for i in range(kn - ln + 1):
        for j in range(kn - ln + 1):
            flag = True
            for x in range(ln):                
                if 0 in (orOper(l[x], k[j + x][j : j + ln])):
                    flag = False
                    break

            if flag:
                return True
    return False

def lstExtend(lst):
    n = len(lst)
    lst = deque(lst)

    for i in range(n):
        lst[i] = deque(lst[i])

    for i in range(n):
        for j in range(n - 1):
            lst[i].appendleft(0)
            lst[i].append(0)

    for i in range(n - 1):
        lst.appendleft([0] * (n + ((n - 1) * 2)))
        lst.append([0] * (n + ((n - 1) * 2)) )

    for i in range(len(lst)):
        lst[i] = list(lst[i])

    return list(lst)

def orOper(lst1, lst2):

    for i in range(3):
        lst1[i] = lst1[i] or lst2[i]
    return lst1

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))