import sys

N, M = map(int, sys.stdin.readline().split())
s = []


def dfs():
    if len(s) == M:
        temp = sorted(s)
        if s == temp:
            print(' '.join(map(str, s)))
            return

    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
