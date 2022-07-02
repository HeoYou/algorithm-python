import copy

input_lst = [list(map(int, input().split())) for i in range(7)]
lst = copy.deepcopy(input_lst)
n = int(input())
chk = [[0] * 7 for i in range(7)]
answer = 100
delete_chk = False

def down():
    global lst, delete_chk
    
    for i in range(6, 0, -1):
        for j in range(7):
            if lst[i][j] == 0:
                lst[i][j] = lst[i - 1][j]
                lst[i - 1][j] = 0

def row():
    global chk, delete_chk
    cnt = 0
    for i in range(7):
        chk_p = 0
        for j in range(7):
            if lst[i][j] == 0:
                for c in range(cnt):
                    if lst[i][chk_p + c] == cnt:
                        chk[i][chk_p + c] = 1
                        delete_chk = True
                cnt = 0
                chk_p = j
            else:
                cnt += 1 
        if cnt == 7:
            for j in range(7):
                if lst[i][j] == 7:
                    chk[i][j] = 1
                    delete_chk = True
                    
def column():
    global chk, delete_chk
    
    for i in range(7):
        cnt = 0
        for j in range(7):
            if lst[j][i] != 0:
                cnt += 1

        # print(cnt)
        for j in range(7):
            if cnt == 0:
                continue
            if lst[j][i] == cnt:
                chk[j][i] = 1
                delete_chk = True
            
                
def delete():
    for i in range(7):
        for j in range(7):
            if chk[i][j] == 1:
                lst[i][j] = 0
          
          

for i in range(7):
    lst = copy.deepcopy(input_lst)
    for j in range(6, -1, -1):
        if lst[j][i] == 0:
            lst[j][i] = n
            break

    delete_chk = True
    

    while delete_chk:
        delete_chk = False
        chk = [[0] * 7 for i in range(7)]
        row()
        column()
        delete()
        down()

    cnt = 0
    for j in range(7):
        for k in range(7):
            if lst[i][j] != 0:
                cnt += 1
    
    answer = min(cnt, answer)
print(answer)