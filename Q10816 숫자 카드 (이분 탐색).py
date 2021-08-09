dic = {}

input()

for n in list(map(int, input().split(' '))):
    if n in dic.keys():
        dic[n] += 1
    else:
        dic[n] = 1
input()
for n in list(map(int, input().split(' '))):
    if n in dic.keys():
        print(dic[n], end=' ')
    else:
        print(0, end=' ')