# s = list(map(int, list(input())))
# answer = [0, 0]
# answer[s[0]] += 1

# for i in range(len(s) - 1):
#     if s[i] != s[i + 1]:
#         answer[s[i + 1]] += 1
        
# print(min(answer))

s = list(input())
answer = [0, 0]
answer[s[0]] += 1

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        answer[s[i + 1]] += 1
        
print(min(answer))