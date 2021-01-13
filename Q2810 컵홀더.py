N = int(input())
seat = input()
count = 0
pos = 0
while pos < N:
    if seat[pos] == 'L':
        count += 1
        pos += 2
    else:
        pos += 1

print(N if N <= 1 else N - count + 1)



N = int(input()) 
seat = input() 
count = seat.count('LL') 
if (count <= 1): 
    print(len(seat)) 
else: 
    print(len(seat) - count + 1)
