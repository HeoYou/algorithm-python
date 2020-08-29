month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #목요일
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
D, M = map(int, input().split())

print(day[(sum(month[:M - 1]) + D + 2) % 7])

