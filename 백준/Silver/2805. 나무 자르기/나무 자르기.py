import sys

r = sys.stdin.readline

n, m = map(int, r().split())

nums = list(map(int, r().split()))
start, end = 1, max(nums)

while start <= end:
    mid = (start + end) // 2
    s = 0

    for i in nums:
        if i >= mid:
            s += i - mid

    if s >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
