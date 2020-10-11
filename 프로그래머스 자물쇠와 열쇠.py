from collections import deque

def solution(key, lock):
    answer = True

    key = lstExtend(key)
    flag = True
    for i in lock:
        if 0 in i:
            flag = False
            break
    if flag:
        return flag

    for _ in range(4):
        lock = rotate_90(lock)
        # for i in range(len(key)):
            # print(key[i])
        # for i in range(len(lock)):
        #     print(lock[i])
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
                # print(l[x], k[i + x][j : j + ln], i, j, x)
                #orOper가 lock배열에 간섭한다 이게 가능한지는 모르겠으나 그런다.
                #그래서 orOper를 수정함
                # if 0 in (orOper(l[x], k[i + x][j : j + ln])):
                if orOper(l[x], k[i + x][j : j + ln]):
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

    flag = False
    for i in range(3):
        if lst1[i] == lst2[i]:
            flag = True
        
        # if lst1[i] == lst2[i]:
        #     lst1[i] = 0
        #     break
        # else:
        #     lst1[i] = 1
    return flag

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))