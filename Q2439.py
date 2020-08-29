n = int(input())

for i in range(n):
    for _ in range(i, n - 1):
        print(" ", end="")

    for _ in range(0, i + 1):
        print("*", end="")

    print("")

for i in range(n):
    print(" " * (n - i - 1) + "*" * (i + 1))