def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if 'A' <= s[i] <= 'Z':
            print(ord(s[i]) + n)
            print(((ord(s[i]) + n) % ord('Z')))
            s[i] = chr((ord(s[i]) + n) % ord('Z') + ord('A') - 1) if (ord(s[i]) + n) >= ord('Z') else chr(ord(s[i]) + n)
        elif 'a' <= s[i] <= 'z':
            s[i] = chr((ord(s[i]) + n) % ord('z') + ord('a') - 1) if (ord(s[i]) + n) >= ord('z') else chr(ord(s[i]) + n)
    print(s)
    return ''.join(s)

print(solution("a Z z", 1))