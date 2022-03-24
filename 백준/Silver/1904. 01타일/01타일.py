import sys

N = int(sys.stdin.readline())
# N의 범위는 1 ~ 100000
dp = [0] * 1000001

# 알려져 있는 값들은 초기화 (N=1 ==> '1' / N = 2 ==> 00, 11)
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])
