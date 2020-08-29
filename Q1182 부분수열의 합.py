N, S = map(int, input().split())

lst = list(map(int, input().split()))
count = 0

for i in range(N):
    sum = 0

    for j in range(i, N):
        sum = sum + lst[j]
        if sum == S:
            count = count + 1
        
print(count)

# N, S = map(int, input().split())

# lst = list(map(int, input().split()))
# count = 0

# for i in range(N):
#     sum = 0
#     for j in range(i, N):
#         sum = sum + j
#         if sum == S:
#             count =+ 1

# print(count)

# N, S = map(int, input().split())

# lst = list(map(int, input().split()))
# count = 0

# for i in range(N):
#     sum = 0

#     for j in range(i, N):
#         sum = sum + lst[j]
#         if sum == S:
#             count =+ 1

# print(count)


# 1. 처음 오답의 원인이 리스트의 값을 더해주어야하는데 반복문의 값을 더해주어 오류가 난걸 확인하였다.
# 2. 두번째 문제는 python언어와 JAVA의 언어구조의 차이를 인식하지못하고 다른 문법을 사용하여 실패하였다고 생각하였다.
# 3. 세번째에선 문제를 애초에 잘못이해하였다. 문제는 부분수열 이라고 하였으나 저는 연속된 부분수열로 착각하여 문제풀이에 실패하였다.
# 4. 아직 문제를 해결하지 못하였으나, 현제 반복문으로 구성된 문제를 재귀함수를 이용해 풀어나갈 예정이다.