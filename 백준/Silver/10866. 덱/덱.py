import sys
from collections import deque as dq

r = sys.stdin.readline

N = int(r())
queue = dq()

for _ in range(N):
    com = list(map(str, r().split()))

    if com[0] == 'push_front':
        queue.appendleft(com[1])
    elif com[0] == 'push_back':
        queue.append(com[1])
    elif com[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(queue))
    elif com[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
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