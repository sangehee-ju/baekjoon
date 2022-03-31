import sys


def two_cnt(x):
    cnt = 0
    while x != 0:
        x //= 2
        cnt += x
    return cnt


def five_cnt(x):
    cnt = 0
    while x != 0:
        x //= 5
        cnt += x
    return cnt


n, m = map(int, sys.stdin.readline().split())

two = two_cnt(n) - two_cnt(n-m) - two_cnt(m)
five = five_cnt(n) - five_cnt(n-m) - five_cnt(m)

print(min(two, five))
