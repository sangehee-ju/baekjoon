import sys

r = sys.stdin.readline
n = int(r())

paper = [list(map(int, r().split())) for _ in range(n)]
m = 0  # -1
z = 0  # 0
o = 0  # 1


def solution(x, y, n):
    global m, z, o
    now = paper[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if now != paper[i][j]:
                solution(x, y, n // 3)
                solution(x, y + n // 3, n // 3)
                solution(x, y + ((n // 3) * 2), n // 3)
                solution(x + n // 3, y, n // 3)
                solution(x + n // 3, y + n // 3, n // 3)
                solution(x + n // 3, y + ((n // 3) * 2), n // 3)
                solution(x + ((n // 3) * 2), y, n // 3)
                solution(x + ((n // 3) * 2), y + n // 3, n // 3)
                solution(x + ((n // 3) * 2), y + ((n // 3) * 2), n // 3)
                return
    if now == -1:
        m += 1
    elif now == 0:
        z += 1
    else:
        o += 1


solution(0, 0, n)
print(m)
print(z)
print(o)
