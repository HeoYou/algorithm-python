def solution(line):
    answer = []
    intersection = []
    lineLen = len(line)
    minx, miny = 1000, 1000
    maxx, maxy = -1000, -1000

    pos = []
    for i in range(lineLen - 1):
        for j in range(i + 1, lineLen):

            # print(line[i])
            # print(line[j])
            if (line[i][0] * line[j][1]) - (line[i][1] * line[j][0]) == 0:
                continue
            x = ((line[i][1] * line[j][2]) - (line[i][2] * line[j][1])) / ((line[i][0] * line[j][1]) - (line[i][1] * line[j][0]))
            y = ((line[i][2] * line[j][0]) - (line[i][0] * line[j][2])) / ((line[i][0] * line[j][1]) - (line[i][1] * line[j][0]))


            # print(x, y)

            if x % 1 == 0 and y % 1 == 0:
                pos.append([int(x), int(y)]) 
                minx = min(minx, int(x))
                miny = min(miny, int(y))
                maxx = max(maxx, int(x))
                maxy = max(maxy, int(y))
    # print(maxx, minx, maxy, miny)
    # print("pos: ", pos)
    answer = [['.'] * (int(maxx) - int(minx) + 1) for _ in range(int(maxy) - int(miny) + 1)]
    # print(answer)
    for x, y in pos:
        # print(x, y)
        answer[y - miny][x - minx] = '*'
    answer = [''.join(i) for i in answer[::-1]]
    

    return answer

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))

