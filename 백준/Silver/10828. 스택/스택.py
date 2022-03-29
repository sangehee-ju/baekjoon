import sys

r = sys.stdin.readline

# 명령의 수
N = int(r())

#스택
stack = []

for _ in range(N):
    comment = r().split()

    if comment[0] == 'push':
        num = int(comment[1])
        stack.append(num)
    elif comment[0] == 'pop':
        N = len(stack)
        if N == 0:
            print(-1)
        else:
            print(stack[N-1])
            stack = stack[:N - 1]
    elif comment[0] == 'size':
        print(len(stack))
    elif comment[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        N = len(stack)
        if N == 0:
            print(-1)
        else:
            print(stack[N - 1])