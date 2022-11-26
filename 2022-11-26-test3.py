# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, S):
    answer = 0
    center_check = [3, 4, 5, 6]
    side_ckeck = [[1, 2, 3, 4], [5, 6, 7, 8]]

    seat = list([0] * 10 for i in range(N + 1))
    
    for i in S.split():
        alpha = ord(i[-1]) - 65
        i = i[:-1]
        seat[int(i)][alpha] = 1
        
    i = 0
    for s in seat[1:]:
        c_count, s_count = 1, 2
        for sc in side_ckeck:
            for s_num in sc:
                if s[s_num] == 1:
                    s_count -= 1
                    break
        for c_num in center_check:
            if s[c_num] == 1:
                c_count -= 1
                break
        
        print(i, max(s_count, c_count), s)
        i += 1
        answer += max(s_count, c_count)
                
            

    return answer
print(solution(22, '1A 3C 2B 20G 5A 10C 10D 10H'))

A, B, C   D, E, F, G   H, J, K