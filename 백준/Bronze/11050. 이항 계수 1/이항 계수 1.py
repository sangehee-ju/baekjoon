import sys

r = sys.stdin.readline

N, K = map(int, r().split())
res = 1

if K > (N / 2):
    K = N - K

for i in range(N, (N-K), -1):
    res *= i

for i in range(K, 0, -1):
    res //= i

print(res)