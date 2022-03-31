import sys


def bio(N, M):
    res = 1
    if N > (M / 2):
        N = M - N

    for i in range(M, (M - N), -1):
        res *= i

    for i in range(N, 0, -1):
        res //= i

    return res


r = sys.stdin.readline

n = int(r())

for _ in range(n):
    N, M = map(int, r().split())
    print(bio(N, M))
