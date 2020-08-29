a = ["A", "B", "C", "D", "E"]
for i in range(3):
    print(a[list(map(int, input().split())).count(0) - 1])