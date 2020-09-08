a,b=map(int,input().split())
count=0
C=abs(a-b)
while C != 0 :
    if C >= 8:
        C = C - 10
        count+=1
    elif C >=3 and C < 8:
        C = C - 5
        count+=1
    elif C < 3 and C >= 1:
        C = C -1
        count+=1
print(count)
