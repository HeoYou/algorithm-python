# 손풀기 문제 틀리면 왜틀린건지 한참 고민해야 할 것이다!!!
# 시간 초과로 틀렸다. 아
# 입력속도다 .아 유레카

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
id, names = dict(), dict()

for i in range(1, n + 1):
    po = input().strip()
    id[i] = po
    names[po] = i
for i in range(m):
    po = input().strip()
    if po.isdigit():
        print(id[int(po)])
    else:
        print(names[po])