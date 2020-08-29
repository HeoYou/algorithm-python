def solution(bridge_length, weight, truck_weights):
    answer = 0

    lengh = [0 for i in range(bridge_length)]
    lengh[0] = truck_weights.pop(0)
    sumlst = [lengh[0]]

    while True:
        answer += 1
        if sum(sumlst) <= 0 and len(truck_weights) <= 0:
            break
            
        if len(truck_weights) > 0 and sum(sumlst) - lengh[-1] + truck_weights[0] <= weight:
            lengh.insert(0, truck_weights[0])
            sumlst.insert(0, truck_weights.pop(0))
            if lengh.pop() == sumlst[-1]:
                sumlst.pop()
        elif len(truck_weights) > 0 and sum(sumlst) - lengh[-1] + truck_weights[0] > weight:
            lengh.insert(0, 0)
            if lengh.pop() == sumlst[-1]:
                sumlst.pop()
        elif len(truck_weights) == 0:
            lengh.insert(0, 0)
            if lengh.pop() == sumlst[-1]:
                sumlst.pop()

    return answer

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

print(solution(bridge_length, weight, truck_weights))