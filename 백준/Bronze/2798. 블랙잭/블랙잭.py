import itertools
import sys

N, M = map(int,sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))
combs = itertools.combinations(nums, 3)
m = 0

for i in combs:
    if M >= sum(i) > m:
        m = sum(i)
print(m)
