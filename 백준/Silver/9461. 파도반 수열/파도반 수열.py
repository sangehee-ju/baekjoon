import sys


def solution(N):
    pd = [0] * 101

    pd[1] = 1
    pd[2] = 1
    pd[3] = 1

    for k in range(4, N + 1):
        pd[k] = pd[k - 3] + pd[k - 2]

    return pd[N]


r = sys.stdin.readline

T = int(r())

for i in range(T):
    N = int(r())
    print(solution(N))
