from math import dist
from turtle import distance


def make_distance(size):
    distance = [[1] * size for _ in range(size)]    
    for i in range(1 ,size):
        for j in range(1, size):
            distance[+j][+i] = distance[+j][+i - 1] + distance[+j - 1][+i]
            distance[+i][+j] = distance[+j][+i - 1] + distance[+j - 1][+i]
    return distance

def solution(width, height, diagonals):
    answer = 0
    distance = make_distance(max(width, height) + 2)
    # for i in distance:
    #     print(i)
    
    for x, y in diagonals:
        mapx = y
        mapy = x - 1
        mapx2, mapy2 = mapx - 1, mapy + 1
        
        # print(mapx, mapy, mapx2, mapy2)
        # print(distance[mapx][mapy])
        # print(distance[mapx2][mapy2])
        # print(distance[width - mapx][height - mapy])
        # print(distance[width - mapx2][height - mapy2])
        answer += (distance[mapx][mapy]) * (distance[width - mapx2][height - mapy2])
        answer += (distance[mapx2][mapy2]) * (distance[width - mapx][height - mapy])

    return answer % 10000019

print(solution(2, 2, [[1,1],[2,2]]))
print(solution(51,37,[[17,19]]))
print(solution(3, 3,[[2, 2],[3,1]]))