import math
import sys

r = sys.stdin.readline

nums = []
a = []
g = 0
for i in range(int(r())):
    nums.append(int(r()))
    if i == 1:
        g = abs(nums[1]-nums[0])
    g = math.gcd(abs(nums[i] - nums[i-1]), g)
g_a = int(g**0.5)
for i in range(2, g_a+1):
    if g % i == 0:
        a.append(i)
        a.append(g // i)
a.append(g)
a = list(set(a))
a.sort()
for i in a:
    print(i,end=' ')

