import sys
input = sys.stdin.readline
lst = []

for _ in range(int(input())):
    commandLine = list(map(str, input().strip().split()))
    command = commandLine[0]


    if command == 'push':
        lst.append(commandLine[1])

    elif command == 'pop':
        if lst:
            print(lst.pop())
        else:
            print(-1)

    elif command == 'size':
        print(len(lst))
    
    elif command == 'empty':
        if lst:
            print(0)
        else:
            print(1)
    
    elif command == 'top':
        if lst:
            print(lst[len(lst) - 1])
        else:
            print(-1)


