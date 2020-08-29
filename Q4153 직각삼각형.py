while True:
    data = list(map(int, input().split()))
    if len(set(data)) == 1:
        break
    data.sort()

    print("right" if data[2] ** 2 == data[0] **2 + data[1] ** 2 else "wrong")