def solution(a, b, go, si, we, ti):

    answer = []
    print(list(zip(go, si, we, ti)))
    for g, s, w, t in list(zip(go, si, we, ti)):

        total_w = 0
        total_w += a - g if a - g >= 0 else 0
        total_w += b - s if b - s >= 0 else 0

        answer.append()
                

    return answer


if __name__=="__main__":
    a = 90
    b = 500
    g = [70,70,0]
    s = [0,0,500]
    w = [100,100,2]
    t = [4,8,1]

    print(solution(a, b, g, s, w, t))