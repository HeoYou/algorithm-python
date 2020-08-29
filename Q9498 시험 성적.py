s = int(input())

# if s // 10 > 8:
#     print("A")
# elif s // 10 > 7:
#     print("B")
# elif s // 10 > 6:
#     print("C")
# elif s // 10 > 5:
#     print("D")
# else:
#     print("F")

score = "FDCBAA"
print(score[0] if s < 60 else score[(s // 10) - 5])
