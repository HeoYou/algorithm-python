n = int(input())
lst = []
for i in range(n ** 2):
    lst.append(list(map(int, input().split())))
    
for i in lst:
    print(i)