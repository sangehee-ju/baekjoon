import sys

r = sys.stdin.readline

for _ in range(int(r())):
    zero = [1, 0]
    one = [0, 1]
    n = int(r())
    if n > 1:
        for i in range(n - 1):
            zero.append(one[-1])
            one.append(zero[-2] + one[-1])

    print(zero[n], one[n])
