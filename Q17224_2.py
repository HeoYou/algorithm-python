N, L, K = map(int, input().split(" "))

easy, hard = 0, 0

answer = 0
for i in range(N):
    sub1, sub2 = map(int, input().split(" "))

    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

answer = min(K, hard) * 140

if K < hard:
    answer += min(K - hard, easy) * 100
