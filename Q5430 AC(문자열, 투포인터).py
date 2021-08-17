import sys
input = sys.stdin.readline

def extraction_num(raw_str):
    if raw_str == '[]':
        return []
    else:
        return list(map(int, raw_str[1:-1].split(',')))
def print_lst(data):
    print('[', end='')
    print(','.join(map(str, data)), end='')
    print(']')

for i in range(int(input())):
    cmd = input().strip()
    n = int(input())
    lst = extraction_num(input().strip())
    rev = 0
    flag = 1
    left, right = 0, len(lst)

    for c in cmd:
        # print(left, right)
        if c == 'R':
            rev = (rev + 1) % 2
        else:
            if left == right:
                print('error')
                flag = 0
                break
            elif not rev:
                left += 1
            elif rev:
                right -= 1
    if flag:
        if rev:
            print_lst(reversed(lst[left:right]))
        else:
            print_lst(lst[left:right])
