#아리토스테네스의 체
import sys
input = sys.stdin.readline

def prime_list(n):
    sieve = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    sieve[0] = False
    sieve[1] = False
    return sieve

answer = 0
num = int(input().strip())
lst = list(map(int, input().strip().split()))
primeLst = prime_list(1000)


for num in lst:
    if primeLst[num]:
        answer += 1

print(answer)
