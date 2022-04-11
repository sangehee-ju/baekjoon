import sys

r = sys.stdin.readline

N = int(r())

vid = [list(r().strip()) for _ in range(N)]
ans = []


def solution(x, y, N):
    global ans
    now = vid[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if now != vid[i][j]:
                ans.append('(')
                solution(x, y, N // 2)
                solution(x, y + N // 2, N // 2)
                solution(x + N // 2, y, N // 2)
                solution(x + N // 2, y + N // 2, N // 2)
                ans.append(')')
                return
    ans.append(now)


solution(0, 0, N)
print(''.join(ans))
