import sys
N, K = map(int, input().split())

answer = 0
jewelLst, bagLst= [], []
for i in range(N):
    jewelLst.append(list(map(int, sys.stdin.readline().split())))
jewelLst = sorted(jewelLst, key = lambda x : x[1], reverse = True)

for i in range(K):
    bagLst.append(int(sys.stdin.readline()))
bagLst = sorted(bagLst, reverse = True)

for i in range(len(bagLst)):
    for j in range(len(jewelLst)):
        if bagLst[i] >= jewelLst[j][0]:
            answer += jewelLst[j][1]
            jewelLst.pop(j)
            break


print(answer)