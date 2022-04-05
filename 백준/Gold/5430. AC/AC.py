import sys
from collections import deque as dq

r = sys.stdin.readline

T = int(r())
for _ in range(T):
    p = list(r().rstrip())
    n = int(r())
    arr = r().rstrip()[1:-1].split(",")
    queue = dq(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0
    if n == 0:
        queue = []
        front = 0
        back = 0

    for i in p:
        if i == 'R':
            rev += 1
        elif i == 'D':
            if len(queue) < 1:
                flag = 1
                print('error')
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 == 0:
            print('['+','.join(queue)+']')
        else:
            queue.reverse()
            print('['+','.join(queue)+']')

