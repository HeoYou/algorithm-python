def solution(stones, k):
    left, right, mid = 0, max(stones), max(stones) // 2
    num_stones = len(stones)
    answer = 0
    while right >= left:
        
        mid = (left + right) // 2
        count = 0

        for i in range(num_stones):
            if mid >= stones[i]:
                count += 1
            else:
                count = 0
            
            if count >= k:
                break

        if count < k:
            left = mid + 1
        else:
            answer = mid
            right = mid - 1

 
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))