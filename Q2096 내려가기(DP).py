# 메모리 제한이 낮다는건 무조건 DP를 사용하라는 거다
# 그리고 DP를 사용해야지 당연히 음음
# ------------------
# dp도 윈도우 슬라이딩 이용해야한다 이거 귀찮아지것네

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

lst = []
min_dp = deque([[0, 0, 0], [0, 0, 0]])
max_dp = deque([[0, 0, 0], [0, 0, 0]])

a, b, c = map(int, input().split())
min_dp[0] = [a, b, c]
max_dp[0] = [a, b, c]

for i in range(n - 1):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_dp[1][j] = max(max_dp[0][0] + a, max_dp[0][1] + a)
            min_dp[1][j] = min(min_dp[0][0] + a, min_dp[0][1] + a)
        elif j == 1:
            max_dp[1][j] = max(max_dp[0][0] + b, max_dp[0][1] + b, max_dp[0][2] + b)
            min_dp[1][j] = min(min_dp[0][0] + b, min_dp[0][1] + b, min_dp[0][2] + b)
        elif j == 2:
            max_dp[1][j] = max(max_dp[0][2] + c, max_dp[0][1] + c)
            min_dp[1][j] = min(min_dp[0][2] + c, min_dp[0][1] + c)
    max_dp.popleft()
    max_dp.append([0, 0, 0])
    min_dp.popleft()
    min_dp.append([0, 0, 0])
print(max(max_dp[0]), min(min_dp[0]))

