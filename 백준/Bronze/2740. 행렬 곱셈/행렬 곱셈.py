import sys

r = sys.stdin.readline


N, M = map(int, r().split())
A = [list(map(int, r().split())) for _ in range(N)]

Nb, Mb = map(int, r().split())
B = [list(map(int, r().split())) for _ in range(Nb)]

res = []
tmp = 0
tmp_li = []

for i in range(N):
    for j in range(Mb):
        for k in range(M):
            tmp += A[i][k] * B[k][j]
        tmp_li.append(tmp)
        tmp = 0
    res.append(tmp_li)
    tmp_li = []

for li in res:
    for i in li:
        print(i, end=' ')
    print()
