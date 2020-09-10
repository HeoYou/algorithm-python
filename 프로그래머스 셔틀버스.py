def sumTime(time, minute):
    h, m = map(int, time.split(':'))
    if m + minute >= 60:
        h += 1
        m = (m + minute) % 60
    else:
        m = (m + minute) % 60
    if h < 10: h = "0" + str(h)
    if m < 10: m = "0" + str(m)
     
    return str(h) + ":" + str(m)
def subTime(time, minute):
    h, m = map(int, time.split(':'))
    if m - minute < 0 :
        h -= 1
        m = (m - minute) % 60
    else:
        m = (m - minute) % 60
    if h < 10: h = "0" + str(h)
    if m < 10: m = "0" + str(m)
     
    return str(h) + ":" + str(m)

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    nowTime = "09:00"
    preTime = 0
    for i in range(n):
        count = 0
        pos = 0

        for j in range(len(timetable)):
            if timetable[j] <= nowTime:
                count += 1
                pos = j
                break
            if j == m:
                break
        
        timetable = timetable[pos:]

        nowTime = sumTime(nowTime, t)
    return answer

print(solution(1, 1, 5, ["09:01", "08:00", "08:01", "08:02", "08:03", "12:12"]))

