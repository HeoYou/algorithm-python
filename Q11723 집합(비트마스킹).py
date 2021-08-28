# import sys
# input = sys.stdin.readline

# dic = set()

# for _ in range(int(input())):
#     cmd = input().split()

#     if len(cmd) == 1:
#         if cmd[0] == 'all':
#             dic = set([i for i in range(1, 21)])
#         else:
#             dic = set()
#     else:
#         if cmd[0] == 'add':
#             dic.add(cmd[1])
#         elif cmd[0] == 'remove':
#             dic.discard(cmd[1])
#         elif cmd[0] == 'check':
#             print(1 if cmd[1] in dic else 0)
#         elif cmd[0] == 'toggle':
#             if cmd[1] in dic:
#                 dic.discard(cmd[1])
#             else:
#                 dic.add(cmd[1])

import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)

