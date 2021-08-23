import sys
input = sys.stdin.readline

dic = set()

for _ in range(int(input())):
    cmd = input().split()

    if len(cmd) == 1:
        if cmd[0] == 'all':
            dic = set([i for i in range(1, 21)])
        else:
            dic = set()
    else:
        if cmd[0] == 'add':
            dic.add(cmd[1])
        elif cmd[0] == 'remove':
            dic.discard(cmd[1])
        elif cmd[0] == 'check':
            print(1 if cmd[1] in dic else 0)
        elif cmd[0] == 'toggle':
            if cmd[1] in dic:
                dic.discard(cmd[1])
            else:
                dic.add(cmd[1])