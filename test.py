def solution(n, arr1, arr2):
    answer = []
    for i in range(n):

        data1 = bin(arr1[i])[2:]

        if len(data1) < n:
            for j in range(n - len(data1)):
                data1 = "0" + data1

        data2 = bin(arr2[i])[2:]
        if len(data2) < n:
            for j in range(n - len(data2)):
                data2 = "0" + data2

        text = ""
        for j in range(n):

            if data1[j] == "1" or data2[j] == "1":
                text += "#"
            elif data1[j] == "0" and data2[j] == "0":
                text += " "

        answer.append(text)
    return answer

arr1 = [46, 33, 33 ,22, 31, 50]
arr2 =[27 ,56, 19, 14, 14, 10]

print(solution(6, arr1, arr2))

print(bin(arr2[3]))