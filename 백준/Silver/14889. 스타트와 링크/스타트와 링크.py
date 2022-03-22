from itertools import combinations as c
import sys

r = sys.stdin.readline

N = int(r())
comb = [i for i in range(N)]
stat = []

for i in range(N):
    stat.append(list(map(int, r().split())))

result = int(1e9)

for c1 in c(comb, N//2):
    start, link = 0, 0
    c2 = list(set(comb) - set(c1))
    for r in c(c1, 2):
        start += stat[r[0]][r[1]]
        start += stat[r[1]][r[0]]

    for r in c(c2, 2):
        link += stat[r[0]][r[1]]
        link += stat[r[1]][r[0]]

    result = min(result, abs(start-link))
print(result)

