from itertools import permutations

def solution(n, k):
    answer = []
    p = permutations([i for i in range(1, n + 1)])
    
    count = 1
    for i in p:
        if count % k == 0:
            return i
        count += 1


print(solution(3, 5))