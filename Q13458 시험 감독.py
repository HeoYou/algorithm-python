N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
sum = 0

for i in A:
    if i <= B:
        sum += 1
    else:
        sum += 1
        if (i - B) % C == 0:
            sum += ((i - B) // C)
        else:
            sum += ((i - B) // C) + 1

print(sum)