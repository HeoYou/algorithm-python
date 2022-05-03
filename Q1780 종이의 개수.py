# import sys
# sys.setrecursionlimit(100000)
# n = int(input())

# data = []
# answer = [0, 0, 0]

# for i in range(n):
#     data.append(list(map(int, input().split())))
# print(type(data[0][0]))

# def paperCount(data):
#     print(1)
#     if len(data) == 1:
#         if data[0] == -1:   answer[0] += 1
#         else:   answer[data[0] + 1] += 1
        
#     else:
#         flag = True
#         num = data[0][0]

#         for i in range(len(data)):
#             if data[i].count(num) != len(data):

#                 flag = False
#                 break
#         if flag:
#             if data[0] == -1:   
#                 answer[0] += 1

#             else:   
#                 answer[data[0][0] + 1] += 1

#         else:
#             for j in range(3):
#                 paperCount([data[k][j * len(data) // 3:(j + 1) * len(data) // 3] for k in range(len(data) // 3)])
#                 paperCount([data[k + (len(data) // 3)][j * len(data) // 3:(j + 1) * len(data) // 3] for k in range(len(data) // 3)])
#                 paperCount([data[k + (len(data) // 3) * 2][j * len(data) // 3:(j + 1) * len(data) // 3] for k in range(len(data) // 3)])

# paperCount(data)
# print(answer)

n = int(input())

answer = [0] * 3
paper = [list(map(int, input().split())) for _ in range(n)]

def chk(lst):
	if len(lst) == 1:
		return True
	num = lst[0][0]
	for l in lst:
		if l.count(num) != len(lst):
			return False
	return True
	
def process(lst):
	global answer
	lenLst = len(lst)
	mid1, mid2 = lenLst // 3, lenLst // 3 * 2

	if chk(lst):
		answer[lst[0][0]] += 1
	else:
		process([i[:mid1] for i in lst[:mid1]])
		process([i[:mid1] for i in lst[mid1:mid2]])
		process([i[:mid1] for i in lst[mid2:]])
		process([i[mid1:mid2] for i in lst[:mid1]])
		process([i[mid1:mid2] for i in lst[mid1:mid2]])
		process([i[mid1:mid2] for i in lst[mid2:]])
		process([i[mid2:] for i in lst[:mid1]])
		process([i[mid2:] for i in lst[mid1:mid2]])
		process([i[mid2:] for i in lst[mid2:]])
		
process(paper)
		
print(answer[-1])
print(answer[0])
print(answer[1])

	