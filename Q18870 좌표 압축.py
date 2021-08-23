import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
lst = list(map(int, input().split()))
lst2 = sorted(list(set(lst)))

for idx, num in enumerate(lst2):
    dic[num] = idx

for i in lst:
    print(dic[i], end=' ')

