def solution(snapshots, transactions):

    account_dic = {}
    remove_overlap = list(set(map(tuple, transactions)))

    for i in snapshots:
        account_dic[i[0]] = int(i[1])
    
    for i in remove_overlap:
        if i[2] not in account_dic:
            account_dic[i[2]] = int(i[3])
        else:
            if i[1] == 'SAVE':
                account_dic[i[2]] += int(i[3])
            elif i[1] =='WITHDRAW':
                account_dic[i[2]] -= int(i[3])
    answer = sorted(account_dic.items())
 
    # answer = list(zip(account_dic2.keys(), account_dic2.values()))
    
    data = []

    for i in answer:
        data.append([i[0], str(i[1])])
    # answer = 0
    return data


snap = [
  ["ACCOUNT2", "150"],  
  ["ACCOUNT1", "100"] 
  
]

transac = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"], 
  ["1", "SAVE", "ACCOUNT2", "100"], 
  ["4", "SAVE", "ACCOUNT3", "500"], 
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

print(solution(snap, transac))


