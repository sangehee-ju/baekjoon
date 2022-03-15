import sys

N = int(sys.stdin.readline())
coordis = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordis.append((y, x))

coordis.sort()

for i in coordis:
    print(i[1], i[0])