from itertools import permutations
import math

def solution_1(n, k):
    answer = []
    p = permutations([i for i in range(1, n + 1)])
    
    count = 1
    for i in p:
        if count % k == 0:
            return i
        count += 1

def solution2(n, k):
    answer = []
    numberLst = [i for i in range(1, n + 1)]

    while(n != 0):
        temp = math.factorial(n)
        print('temp', temp)
        index = k // temp
        print('index', index)
        k = k % temp
        print('k', k)
        if k == 0:
            answer.append(numberLst.pop(index-1))
        else:
            answer.append(numberLst.pop(index))

        n -= 1
    return answer

def solution(n, k):
    answer = []
    numberLst = [i for i in range(1, n + 1)]

    while(n != 0):
        temp = math.factorial(n)
        #print('temp ', temp)
        pop_pos = k % n
        #print('pop_pos ', pop_pos)
        k = k // temp
        #print('k ', k)
        if k:
            answer.append(numberLst.pop(pop_pos - 1))
        else:
            answer.append(numberLst.pop(pop_pos))
        n -= 1
    return answer

print(solution(3, 5))