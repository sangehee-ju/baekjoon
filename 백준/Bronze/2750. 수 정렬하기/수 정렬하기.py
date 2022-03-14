import sys

N = int(sys.stdin.readline())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline()))

for i in range(N):
    temp = 0
    for j in range(N):
        if nums[i] < nums[j]:
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

for i in nums:
    print(i)