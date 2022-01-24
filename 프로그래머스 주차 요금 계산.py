def ret_minute(t):
    h, m = t.split(':')
    minute = int(h) * 60 + int(m)
    return minute

def calc_fee(fees, park_time):
    if fees[2] == 1:
        return fees[1] if park_time < fees[0] else ((park_time - fees[0]) // fees[2] * fees[3]) + fees[1]
    else:
        return fees[1] if park_time < fees[0] else ((park_time + fees[2] - 1 - fees[0]) // fees[2] * fees[3]) + fees[1]

def solution(fees, records):
    cars_stack = {}
    answer_dic = {}

    for rec in records:
        t, num, state = rec.split()
        if state == 'IN':
            cars_stack[num] = t
        else:
            park_time = ret_minute(t) - ret_minute(cars_stack[num])
            if answer_dic.get(num):
                answer_dic[num] += park_time
            else:
                answer_dic[num] = park_time
            cars_stack[num] = False
            

    for k in cars_stack.keys():
        if cars_stack[k]:
            park_time = 1439 - ret_minute(cars_stack[k])
            if answer_dic.get(k):
                answer_dic[k] += park_time
            else:
                answer_dic[k] = park_time
            
    return [calc_fee(fees, answer_dic[idx]) for idx in sorted(answer_dic.keys())]

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))
# print(calc_fee(fees, 334))