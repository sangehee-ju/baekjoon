import sys


def c(x, r):
    a = 1
    if x < r:
        return 0
    elif x == r:
        return 1

    for i in range(1, r + 1):
        a *= (x - i + 1)
        a //= i
    return a


N, K, M = map(int, sys.stdin.readline().split())

ni = []
ki = []
cnt = 0
while N != 0 and K != 0:
    ni.append(N % M)
    ki.append(K % M)

    N //= M
    K //= M

ans = 1
for i in range(len(ni)):
    ans *= c(ni[i], ki[i])
    ans %= M

print(ans)
