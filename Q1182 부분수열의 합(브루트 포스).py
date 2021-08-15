# 옛날에 풀지 못했던 문제이다 .. 문제를 잘못이해한 것 같은데 브루트포스 이번엔 한번 풀어봐야할것같다.
# 부분수열의 정의를 정확히 알지 못하고 있음 
# 부분수열이란 연속된게 아니라 그냥 상대적 순서만 가지고 있으면 된다..
# 이 문제를 해결하려면 재귀적인 풀이가 필요해 보인다. 근데 도저히 감이 안잡힌다.

n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))

answer = 0

for i in range(n):
    for j in range(i + 1, n):
        if sum(lst[i:j]) == m:
            answer += 1
answer += lst.count(m)
print(answer)
