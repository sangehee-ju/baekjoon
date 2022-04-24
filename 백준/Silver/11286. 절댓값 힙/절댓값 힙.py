import sys
import heapq as hp

r = sys.stdin.readline

n = int(r())
heap = []

for _ in range(n):
    c = int(r())
    if c:
        hp.heappush(heap, (abs(c), c)) # ()(튜플) 형테로 heap에 입력, (abs, original)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(hp.heappop(heap)[1])
