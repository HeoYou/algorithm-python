def solution(numbers, hand):
    answer = ''
    lpos, rpos = [0, 3], [0, 3]
    left, right = [1, 4, 7], [3, 6, 9]
    mid = [2, 5, 8, 0]


    def distinct(pos, g):
        nonlocal mid
        ans = 0
        if pos[0] == 0:
            ans = 1 + abs(pos[1] - mid.index(g))
        elif pos[0] == 1:
            ans = abs(pos[1] - mid.index(g))
        return ans

    for i in numbers:
        if i in left:
            answer += 'L'
            lpos = [0, left.index(i)]
        elif i in right:
            answer += 'R'
            rpos = [0, right.index(i)]
        else:
            if distinct(lpos, i) == distinct(rpos, i):
                answer += hand[0].upper()
                if hand[0] == 'r':
                    rpos = [1, mid.index(i)]
                else:
                    lpos = [1, mid.index(i)]
            elif distinct(lpos, i) > distinct(rpos, i):
                answer += 'R'
                rpos = [1, mid.index(i)]
            else:
                answer += 'L'
                lpos = [1, mid.index(i)]
            
        print(lpos, rpos)
    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))