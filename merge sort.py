import sys

n = int(sys.stdin.readline())

data = []
for _ in range(n):
    data.append(int(sys.stdin.readline()))

def mergeSort(arrData):
    fullData = []
    if len(arrData) > 1:
        mid = len(arrData) // 2
        leftData = arrData[:mid]
        rightData = arrData[mid:]

        leftData =  mergeSort(leftData)
        rightData =  mergeSort(rightData)
        i = 0
        j = 0
        k = 0

        while leftData or rightData:

            if not leftData:
                while rightData:
                    fullData.append(rightData.pop(0))
            elif not rightData:
                while leftData:
                    fullData.append(leftData.pop(0))
            else:
                if leftData[0] >= rightData[0]:
                    fullData.append(rightData.pop(0))
                else:
                    fullData.append(leftData.pop(0))

    else:
        fullData.append(arrData.pop(0))

    return fullData

data = mergeSort(data)
for i in data:
    print(i)

