def solution(record):
    answer = []

    name = {}

    for arr in record:
        list = arr.split(" ")
        if list[0] != "Leave":
            name[list[1]] = list[2]

    for arr in record:
        list = arr.split(" ")

        if list[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(name[list[1]]))
        elif list[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(name[list[1]]))

    return answer

data = ["Enter uid1234 Muzi", "Enter uid2345 con", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(data))