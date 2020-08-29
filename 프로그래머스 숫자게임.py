def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    A_idx = 0
    for i in range(len(A)):
        if B[i] > A[A_idx]:
            answer += 1
            A_idx += 1

    return answer

print(solution([5,1,3,7], [2,2,6,8]))