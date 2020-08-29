lstSum = []
for i in range(5):
   lstSum.append(sum(map(int, input().split())))
print(lstSum.index(max(lstSum)) + 1, max(lstSum))