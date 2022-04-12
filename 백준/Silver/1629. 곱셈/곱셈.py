import sys

# 지수법칙 : a^m * b^n = a^(m+n)
# 나머지 분배법칙 : (a*b) % c = (a%c)*(b%c) % c
# 위 두 법칙을 활용하여 풀 수 있는 문제


r = sys.stdin.readline

a, b, c = map(int, r().split())


def solution(a, b):
    if b == 1:
        return a % c

    else:
        temp = solution(a, b//2)
        if b % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c


print(solution(a, b))
