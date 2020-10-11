import sys

n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))

crane = sorted(crane, reverse = True)
box = sorted(box, reverse = True)

if crane[0] < box[0]:
    print(-1)
    sys.exit()
    
