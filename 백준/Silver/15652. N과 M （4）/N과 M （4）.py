import sys

r = sys.stdin.readline

N, M = map(int, r().split())

s = []


def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N + 1):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)
