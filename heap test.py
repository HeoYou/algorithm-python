# 일반적인 리스트를 최소 힙처럼 다룰 수 있도록 도와준다.
import heapq

print()
print("최소힙 일반적")
# 리스트를 생성하고 heapq를 이용하여 원소를 추가하거나 삭제한다.
heap = []

heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
heapq.heappush(heap, 7)

print(heapq.heappop(heap))
print(heap)
print(heap[0])

heap = [4, 1, 7, 9, 8, 3]
heapq.heapify(heap)
print(heap)


print()
print("최대힙")
#최대 힙 heapq모듈은 최소 힙기능만해서 최대힙을 사용하려면 약간의 요령이 필요하다.
#힙에 튜플을 원소로 추가하거나 삭제하면 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용

nums = [4, 1, 7, 3, 8, 5]
heap = []


for num in nums:
    heapq.heappush(heap, (-num, num))
print(heap)

while heap:
    print(heapq.heappop(heap)[1])

print()
print("k번째")
#K번째 최소값/최대값
def kth_smallest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)

    kth_min = 0
    for _ in range(k):
        kth_min = heapq.heappop(heap)
    return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))


def kth_biggest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, (-num, num))

    kth_min = None
    for _ in range(k):
        kth_min = heapq.heappop(heap)[1]
    return kth_min

print(kth_biggest([4, 1, 7, 3, 8, 5], 3))
