def solution(files):

    files = [[i] for i in files]

    for i in range(len(files)):
        num = ""
        for j in range(len(files[i][0])):
            if files[i][0][j] in "0123456789":
                files[i].append(files[i][0][0:j].lower())
                break
        for j in range(len(files[i][1]), len(files[i][0])):
            if files[i][0][j] in "0123456789":
                num = num + files[i][0][j]
            else:
                break
        files[i].append(int(num))
    
    files = sorted(sorted(files, key = lambda x : x[2]), key = lambda x : x[1])
    
    answer = [i[0] for i in files]
    return answer

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))