n = int(input())
nc = n * 2 + 1
c = int(input())
input_string = input()
p = "I" + "OI" * n

answer = 0

for i in range(c - nc):
    if p == input_string[i : i + nc]:
        answer += 1
        
print(answer)