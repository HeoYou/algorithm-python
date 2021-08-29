# 이렇게 풀리면 개꿀 골4가 아닐꺼야...
# a = input()
# b = input()
# while a.count(b) > 0:
#     a = a.replace(b, '')

# print(a if a else 'FRULA')


# 1번째 풀이 시간초과 
# s = list(input())
# comp = list(input())

# stack = []
# last_comp = comp[-1]
# len_comp = len(comp)

# for i in s:
#     stack.append(i)
#     if last_comp == stack[-1]:
#         if len(stack) >= len_comp:
#             if stack[-len_comp:] == comp[:]:
#                 stack = stack[:-len_comp]


# print(''.join(stack) if stack else 'FRULA')

# 그냥 리스트를 복사하는게 문제였따. del 을쓰자
s = list(input())
comp = list(input())

stack = []
last_comp = comp[-1]
len_comp = len(comp)

for i in s:
    stack.append(i)
    if last_comp == stack[-1]:
        if stack[-len_comp:] == comp[:]:
            del stack[-len_comp:]


print(''.join(stack) if stack else 'FRULA')