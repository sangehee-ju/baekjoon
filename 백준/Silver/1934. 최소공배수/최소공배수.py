import sys


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


r = sys.stdin.readline

T = int(r())

for _ in range(T):
    m, n = map(int, r().split())
    print(lcm(m, n))
