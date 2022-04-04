import sys
from collections import deque

r = sys.stdin.readline

n, k = map(int, r().split())
queue = [i for i in range(1, n + 1)]
answer = []
num = k - 1

for i in range(n):
    if len(queue) > num:
        answer.append(queue.pop(num))
        num += k - 1
    elif len(queue) <= num:
        num %= len(queue)
        answer.append(queue.pop(num))
        num += k - 1

print('<', ', '.join(str(i) for i in answer), '>', sep='')
