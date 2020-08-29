import sys
sys.setrecursionlimit(100000)
n = int(input())

data = []
answer = [0, 0, 0]

for i in range(n):
    data.append(list(map(int, input().split())))
print(type(data[0][0]))

def paperCount(data):
    print(1)
    if len(data) == 1:
        if data[0] == -1:   answer[0] += 1
        else:   answer[data[0] + 1] += 1
        
    else:
        flag = True
        num = data[0][0]

        for i in range(len(data)):
            if data[i].count(num) != len(data):

                flag = False
                break
        if flag:
            if data[0] == -1:   
                answer[0] += 1

            else:   
                answer[data[0][0] + 1] += 1

        else:
            for j in range(3):
                paperCount([data[k][j * len(data) // 3:(j + 1) * len(data) // 3] for k in range(len(data) // 3)])
                paperCount([data[k + (len(data) // 3)][j * len(data) // 3:(j + 1) * len(data) // 3] for k in range(len(data) // 3)])
                paperCount([data[k + (len(data) // 3) * 2][j * len(data) // 3:(j + 1) * len(data) // 3] for k in range(len(data) // 3)])

paperCount(data)
print(answer)

