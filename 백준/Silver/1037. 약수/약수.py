import sys

r = sys.stdin.readline

N = int(r())
nums = list(map(int, r().split()))

if len(nums) == 1:
    print(nums[0]**2)
else:
    nums.sort()
    print(nums[0]*nums[N-1])

