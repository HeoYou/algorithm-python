def solution(num_teams, remote_tasks, office_tasks, employees):
    
    answer = []
    # 재택이 True
    team_check = [True] * (num_teams + 1)
    emp_check = [True] * (len(employees) + 1)
    
    
    for idx, e in enumerate(employees):
        e = e.split()
        print(idx + 1, e)
        
        for t in e[1:]:
            if t in office_tasks:
                team_check[int(e[0])] = False
                emp_check[idx + 1] = False
                break
    
    for idx, tc in enumerate(team_check[1:]):
        if tc == True:
            for i, e in enumerate(employees):
                e = e.split()
                if e[0] == str(idx + 1):
                    emp_check[i + 1] = False
                    break
    
    
    
    for idx, v in enumerate(emp_check[1:]):
        if v == True:
            answer.append(idx + 1)
    
    
    return sorted(answer)


num_teams = 3
remote_tasks = ["development","marketing","hometask"]
office_tasks = ["recruitment","education","officetask"]
employees = ["1 development hometask","1 recruitment marketing","2 hometask","2 development marketing hometask","3 marketing","3 officetask","3 development"]
print(solution(num_teams, remote_tasks, office_tasks, employees))