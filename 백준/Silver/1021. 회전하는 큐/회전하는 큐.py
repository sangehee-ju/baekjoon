import sys
from collections import deque as dq

r = sys.stdin.readline

N, M = map(int, r().split())
position = list(map(int, r().split()))
queue = dq(i for i in range(1, N+1))

cnt = 0

for i in position:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue) / 2:
                cnt += 1
                queue.append(queue.popleft())
            else:
                cnt += 1
                queue.appendleft(queue.pop())

print(cnt)