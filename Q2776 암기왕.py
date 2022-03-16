import sys
imput = sys.stdin.readline


for _ in range(int(input())):

    num_c = int(input())
    nums = sorted(list(map(int, input().split())))
    find_c = int(input())
    find_lst = list(map(int, input().split()))
    for n in find_lst:
        l, r, m = 0, num_c - 1,(len(nums) -1) // 2
        flag = True
        while l <= r:
            # print("in", l, r, m)
            if n == nums[m]:
                print(1)
                flag = False
                break
            elif n > nums[m]:
                l = m + 1
                m = (l + r) // 2
            elif n < nums[m]:
                r = m - 1
                m = (l + r) // 2
        if flag:
            print(0)


    # print(num_c, nums, find_c, find_lst)

