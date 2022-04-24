# 파이썬을 이용해 문제를 풀이하므로, 파이썬에 내장된 heapq을 활용한다.
# 하지만, min heap만 지원하므로, 음수로 바꾸어 절대값이 가장 큰 값이 가장 작아지도록 한다.

import sys

import heapq as hp

r = sys.stdin.readline

n = int(r())
heap = []

for _ in range(n):
    c = int(r())
    if c:
        hp.heappush(heap, -c) # 이를 위해, 입력 받은 값에 음수를 취해 heap에 입력한다.
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(-1*hp.heappop(heap)) # 그 후, 출력 시 다시 음수를 취해 결과값을 원상복귀 한다.
