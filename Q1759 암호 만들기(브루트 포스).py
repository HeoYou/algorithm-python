# combination을 만들줄 말라서 우선 있는거 사용했다...
# 시간초과나 메모리를 엄청 먹을줄 알았는데 꼭 그렇지도 않다 나이스


from itertools import permutations, combinations

n, m = map(int, input().split())
lst = sorted(list(map(str, input().split())))
answer = []

combi = list(map(''.join, combinations(lst,n)))

for c in combi:
    j, m = 0, 0
    for s in c:
        if s in 'aeiou':
            m += 1
        else:
            j += 1
    if j >= 2 and m >= 1:
        answer.append(c)

for i in answer:
    print(i)