import sys

r = sys.stdin.readline

n = int(r())

stack = []
answer = []

flag = 0
cur = 1

for i in range(n):
    num = int(r())
    while cur <= num: # 입력한 수를 만날때 까지 오름차순으로 push
        stack.append(cur)
        answer.append('+')
        cur += 1
    # 입력한 수를 만나면 while문 탈출. 즉, cur = num일 때까지 while문을 돌아 스택을 쌓는다.

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)