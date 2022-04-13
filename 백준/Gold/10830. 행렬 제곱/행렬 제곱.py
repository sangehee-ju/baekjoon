import sys

r = sys.stdin.readline

N, B = map(int, r().split())
mx = [list(map(int, r().split())) for _ in range(N)]


def mul(x, y):
    n = len(x)
    z = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += x[row][i] * y[i][col]
            z[row][col] = e % 1000

    return z

def square(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A

    tmp = square(A, B//2)
    if B%2:
        return mul(mul(tmp, tmp),A)
    else:
        return mul(tmp, tmp)

result = square(mx, B)
for r in result:
    print(*r)
