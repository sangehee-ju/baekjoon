import sys

r = sys.stdin.readline

n = int(r())
stack = []

for _ in range(n):
    num = int(r())

    if num == 0 and len(stack) > 0:
        stack = stack[:-1]
    else:
        stack.append(num)

print(sum(stack))