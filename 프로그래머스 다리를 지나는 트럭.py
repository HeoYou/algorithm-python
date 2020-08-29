def solution(bridge_length, weight, truck_weights):
    answer = 1

    lengh = [0 for i in range(bridge_length)]
    lengh[0] = truck_weights.pop(0)

    while True:
  

        if sum(lengh) == 0 and sum(truck_weights) == 0:
            break

        if len(truck_weights) > 0 and sum(lengh) + truck_weights[0] <= weight:
            lengh.insert(0, truck_weights.pop(0))
            lengh.pop()
        
        elif len(truck_weights) > 0 and sum(lengh) + truck_weights[0] > weight:
            lengh.insert(0, 0)
            lengh.pop()

        elif len(truck_weights) == 0:
            lengh.insert(0, 0)
            lengh.pop()
        answer += 1

    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))