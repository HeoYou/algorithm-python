n = int(input())

data = list(map(int, input().split()))
count = 0

def dfs(sum, nextData):
    global count

    sum = sum + data[nextData]
    print(sum)
    if sum == 0:
        count += 1

    if nextData >= n - 1:
        return
    
    dfs(sum, nextData + 1)
    dfs(sum, nextData + 1)



for i in range(n):
    dfs(0, i)

print(count)