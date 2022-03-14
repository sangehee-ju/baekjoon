import sys

N = int(sys.stdin.readline())
bulk = []
rank = [0] * N

for i in range(N):
    m, h = map(int, sys.stdin.readline().split())
    bulk.append((h, m))

for i in range(len(bulk)):
    cnt = 1
    for j in bulk:
        if bulk[i][0] < j[0]:
            if bulk[i][1] < j[1]:
                cnt += 1

    rank[i] = cnt

for i in rank:
    print(i,end=' ')
