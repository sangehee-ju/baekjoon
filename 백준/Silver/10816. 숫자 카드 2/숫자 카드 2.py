import sys

r = sys.stdin.readline

N = int(r())
cards = list(map(int, r().split()))
cards.sort()

M = int(r())
targets = list(map(int, r().split()))

count = {}

for i in cards:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for target in targets:
    result = count.get(target)
    if not result:
        print(0, end=' ')
    else:
        print(result, end=' ')
