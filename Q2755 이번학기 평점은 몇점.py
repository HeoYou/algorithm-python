creditSum = 0
gradeSum = 0.0

grade = {
            "A+": 4.3, "A0": 4.0, "A-": 3.7, 
            "B+": 3.3, "B0": 3.0, "B-": 2.7, 
            "C+": 2.3, "C0": 2.0, "C-": 1.7, 
            "D+": 1.3, "D0": 1.0, "D-": 0.7,
            "F": 0.0
        }

for i in range(int(input())):
    _, b, c = map(str, input().split())
    creditSum += int(b)
    gradeSum += grade[c] * int(b)

answer = gradeSum / creditSum


if int(answer * 1000) % 10 > 4:
    answer = int(answer * 100 + 1) / 100


print('%.2f' % answer)