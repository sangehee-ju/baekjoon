import math
import sys

input = sys.stdin.readline()

A, B, V = map(int, input.split())

res = (V - B) / (A - B)

print(math.ceil(res))
