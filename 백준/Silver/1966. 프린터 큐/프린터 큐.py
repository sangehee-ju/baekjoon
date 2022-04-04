import sys
from collections import deque

r = sys.stdin.readline

T = int(r())

for _ in range(T):
    N, M = map(int, r().split())
    queue = deque(list(map(int, r().split())))
    cnt = 0

    while queue:
        best = max(queue) # 현재의 최댓값이 가장 먼저 배출되므로 최댓값 저장
        front = queue.popleft() # 큐의 front를 뽑았으므로
        M -= 1 # 찾고자 하는 수의 위치를 당겨준다

        if best == front: # 뽑은 숫자가 가장 큰 수이면
            cnt += 1 # 하나가 pop되므로 cnt 하나 추가
            if M < 0: # M이 0이라는 것은 뽑은 숫자가 찾고있는 숫자라는 의미
                print(cnt)
                break

        else: # 뽑은 숫자가 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로 밀려난다.
            if M < 0: # 제일 앞에서 뽑히면
                M = len(queue) - 1 # 제일 뒤로 이동
