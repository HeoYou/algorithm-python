import sys

n = int(input())
k = int(input())
lstTmp = [0] * (n - 1)

lst = list(map(int, input().split()))
lst.sort()

if n <= k:
    print(0)
    sys.exit()


for i in range(n - 1):
    lstTmp[i] = lst[i + 1] - lst[i]
lstTmp.sort(reverse = True)
for i in range(k - 1):
    lstTmp[i] = 0


print(sum(lstTmp)) 
