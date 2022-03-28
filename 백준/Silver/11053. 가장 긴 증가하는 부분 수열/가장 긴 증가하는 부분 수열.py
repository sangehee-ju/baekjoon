import sys

r = sys.stdin.readline

N = int(r())

nums = list(map(int, r().split()))
dp = [0 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
