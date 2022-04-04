import sys
from collections import deque

N = int(sys.stdin.readline())

queue = deque(i for i in range(1, N+1))

while True:
    if len(queue) == 1:
        print(queue.pop())
        break

    queue.popleft()
    queue.append(queue.popleft())
