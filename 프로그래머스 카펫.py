def solution(b, r):

    width = b + r
    for i in range(b, -1, -1):
        if width % i == 0 and 2 * (i + width // i) - 4 == b:
            return [i, width // i]
