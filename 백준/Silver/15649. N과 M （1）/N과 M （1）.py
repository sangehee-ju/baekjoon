# 백트래킹 알고리즘
import sys

N, M = map(int, sys.stdin.readline().split())

# s : 현재의 순열을 담는 리스트
s = []


def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()


dfs()
