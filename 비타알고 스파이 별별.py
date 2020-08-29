# N, m = map(int, input().split())
# lst = list(map(int, input().split()))

# maxAns = 0

# for i in range(1, N):
#     maxAns = max((sum(lst[:i]) % m) + (sum(lst[i:]) % m), maxAns)

# print(maxAns)

N, m = map(int, input().split())
lst = list(map(int, input().split()))

maxAns = 0
l = sum(lst)
r = 0

for i in range(N - 1 , 0, -1): #1 까지의 범위를 0으로 수정후 통과.
    l = l - lst[-i]
    r = r + lst[-i]

    maxAns = max(maxAns, (l % m) + (r % m))

print(maxAns)

# 처음에는 모두 썸으로 더하려다 시간초과가 걸린다.
# 두번째 시도에 무도 sum으로 더하려는걸 리스트에서 한개씩 빼고 더해서 시간 초과를 해결
# 하지만 한개의 테스트케이스에서 오답이난다. 반복문의 범위문제로 생각된다.
# 모든 케이스 통과함. 생각대로 반복문의 범위문제였다.