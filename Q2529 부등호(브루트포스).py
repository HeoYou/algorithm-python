import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
sign = list(map(str, input().split()))

answer = []

def dfs(count, num):
    global answer

    if count >= n :
        answer.append(num)
        return

    for i in range(10):
        if sign[count] == '<':
            if int(num[count]) < i and str(i) not in num:
                dfs(count + 1, num + str(i))

        elif sign[count] == '>':
            if int(num[count]) > i and str(i) not in num:
                dfs(count + 1, num + str(i))

for i in range(10):
    dfs(0, str(i))

print(answer[-1])
print(answer[0])


# def dfs1(lst):
#     if len(lst) == 5:
#         print(lst)
#         return

#     for i in range(5):
#         lst.append(i)
#         dfs1(lst)

# dfs1([])