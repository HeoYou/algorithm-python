# 뭔가 심사 숙고하고 이런 답을 얻어냈을거라 생각함 

# n = int(input())

# answer = 9

# for i in range(1, n):
#     answer = answer * 2 - i
# print(answer // 1000000000)


# 우선 재귀를 사용하는건 답이아니다
# 이걸 이용해야지

import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
answer = 0

def dfs(nums):
    global answer
    if len(nums) == n:
        answer += 1
        return

    if int(nums[-1]) == 0:
        dfs(nums + '1')
    elif int(nums[-1]) == 9:
        dfs(nums + '8')
    else:
        dfs(nums + str(int(nums[-1]) - 1))
        dfs(nums + str(int(nums[-1]) - 1))

for i in range(1, 10):
    dfs(str(i))
print(answer % 1000000000)