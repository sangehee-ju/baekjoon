import sys

r = sys.stdin.readline

N = int(r())
nums = list(map(int, r().split()))
nums.sort()
leng = len(nums)

M = int(r())
finds = list(map(int, r().split()))

for i in finds:
    left = 0
    right = leng - 1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == i:
            flag = True
            print(1)
            break
        elif nums[mid] > i:
            right = mid - 1
        else:
            left = mid + 1

    if not flag:
        print(0)
