N, S = int(input()), input()

score, bonus = 0, 0

for idx, i in enumerate(S):
    if i == "O":
        score = score + idx + bonus + 1
        bonus += 1

    else:
        bonus = 0

print(score)
