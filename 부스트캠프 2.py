def solution(arrA, arrB):
    answer = []
    
    setA = toSet(arrA)
    answer.append(len(setA))
    setB = toSet(arrB)
    answer.append(len(setB))
    answer.append(sum(setA, setB))
    answer.append(complement(setA, setB))
    setA = toSet(arrA)
    answer.append(intersect(setA, setB))



    return answer


def sum(aA, aB):
    answer = []

    answer = toSet(aA + aB)

    return len(answer)

def complement(aA, aB):
    answer = aA[:]

    for i in aB:
        if i in answer:
            answer.remove(i)

    return len(answer)

def intersect(aA, aB):
    answer = []

    for i in aA:
        if i in aB:
            answer.append(i)

    return len(answer)

def toSet(arr):
    answer = []

    for i in arr:
        if i not in answer:
            answer.append(i)
    return answer

aaA = 	[1, 2, 3, 2, 1]
aaB = [1, 3]

print(solution(aaA, aaB))
print('"' + '", "'.join([str(i) for i in range(1000, 2000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(2000, 3000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(3000, 4000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(4000, 5000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(5000, 6000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(6000, 7000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(7000, 8000)]) + '"')
print('"' + '", "'.join([str(i) for i in range(8000, 9000)]) + '"')

