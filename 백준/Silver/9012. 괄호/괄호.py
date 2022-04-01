# VPS : Valid Parenthesis String (올바른 괄호 문자열)
import sys

r = sys.stdin.readline

N = int(r())

for _ in range(N):
    s = list(r())
    su = 0

    for b in s:
        if b == '(':
            su += 1
        elif b == ')':
            su -= 1
        if su < 0:
            print('NO')
            break
    if su > 0:
        print('NO')
    elif su == 0:
        print('YES')