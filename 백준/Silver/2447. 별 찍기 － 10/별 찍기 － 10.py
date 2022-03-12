import sys


def get_stars(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return matrix


stars = ['***', '* *', '***']
n = int(sys.stdin.readline())
e = 0

while n != 3:
    n = int(n / 3)
    e += 1

for i in range(e):
    stars = get_stars(stars)
for i in stars:
    print(i)
