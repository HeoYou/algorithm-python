startTime = list(map(int, input().split(":")))
endTime = list(map(int, input().split(":")))

#60분을 넘어서 시간이 1 올라갈경우 시간차이는 1 
#startTime에서 9를 더해주고 60으로 나머지를 계산 그리고 endTime을 뺴주면 분의 차이를 알 수 있다.
if endTime[0] - startTime[0] == 1 and (startTime[1] + 9) % 60 - endTime[1] < 10:
    print(1)
#startTime - endTime
elif endTime[0] - startTime[0] == 0 and endTime[1] - startTime[1] < 10:
    print(1)
else:
    print(0)


startTime = list(map(int, input().split(":")))
endTime = list(map(int, input().split(":")))

print(startTime[0], startTime[1])
