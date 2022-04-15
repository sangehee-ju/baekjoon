import sys
from collections import deque

r = sys.stdin.readline

while True:
    tmp_li = list(map(int, r().split()))
    n = tmp_li.pop(0)

    if n == 0:
        break

    stack = deque()
    answer = 0

    # 왼쪽부터 차례대로 탐색
    for i in range(n):
        while len(stack) != 0 and tmp_li[stack[-1]] > tmp_li[i]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1] - 1
            answer = max(answer, width*tmp_li[tmp])
        stack.append(i)



    # 스택에 남아있는 것 처리
    while len(stack) != 0:
        tmp = stack.pop()
        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1] - 1
        answer = max(answer, width * tmp_li[tmp])

    print(answer)
