import sys
from collections import deque

r = sys.stdin.readline

N = int(r())
queue = deque()

for _ in range(N):
    com = list(map(str, r().split()))

    if com[0] == 'push':
        queue.append(com[1])

    elif com[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif com[0] == 'size':
        print(len(queue))

    elif com[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif com[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif com[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
