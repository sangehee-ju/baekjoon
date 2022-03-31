import sys

r = sys.stdin.readline

T = int(r())


for _ in range(T):
    closet = dict()
    k = []
    temp = 1
    for _ in range(int(r())):
        cloth, kind = r().split()
        if closet.get(kind) is None:
            closet.setdefault(kind, [cloth])
            k.append(kind)
        else:
            closet[kind].append(cloth)

    for i in k:
        temp *= len(closet[i]) + 1
    print(temp - 1)
