def solution(logs):
    
    answer = 0
    
    for l in logs:
        if len(l) > 100:
            answer += 1
            continue
        
        l = l.split(" ")
        if len(l) != 12:
            answer += 1
        elif l[0] !=  "team_name":
            answer += 1
        elif l[3] !=  "application_name":
            answer += 1
        elif l[6] !=  "error_level":
            answer += 1
        elif l[9] !=  "message":
            answer += 1
        elif not l[2].isalpha():
            answer += 1
        elif not l[5].isalpha():
            answer += 1
        elif not l[8].isalpha():
            answer += 1
        elif not l[11].isalpha():
            answer += 1
    return answer

logs = ["team_name : MyTeam application_name : YourApp error_level : info messag : IndexOutOfRange", "no such file or directory", "team_name : recommend application_name : recommend error_level : info message : RecommendSucces11", "team_name : recommend application_name : recommend error_level : info message : Success!", "   team_name : db application_name : dbtest error_level : info message : test", "team_name     : db application_name : dbtest error_level : info message : test", "team_name : TeamTest application_name : TestApplication error_level : info message : ThereIsNoError"]
print(solution(logs))