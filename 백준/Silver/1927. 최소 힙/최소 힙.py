import sys
import heapq as hp # min heap 지원

r = sys.stdin.readline

n = int(r())
heap = []

for _ in range(n):
    c = int(r())

    if c:
        hp.heappush(heap, c)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(hp.heappop(heap))
