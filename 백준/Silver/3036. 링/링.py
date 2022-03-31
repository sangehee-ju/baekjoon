import sys

r = sys.stdin.readline

N = int(r())
nums = list(map(int, r().split()))

for i in range(N-1):
    x = nums[0]
    y = nums[i+1]
    while x % y != 0:
        r = x % y
        x = y
        y = r
    denom = nums[0] // y
    number = nums[i+1] // y
    print(f'{denom}/{number}')
