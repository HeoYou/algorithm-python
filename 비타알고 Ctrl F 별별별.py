import time

data = input()
findData = input()
timeStart = time.time()



# for i in range(len(data) - len(findData) + 1):
#     if data[i:i + len(findData)] == findData:
#         print(i + 1)

print("time : ", time.time() - timeStart)
