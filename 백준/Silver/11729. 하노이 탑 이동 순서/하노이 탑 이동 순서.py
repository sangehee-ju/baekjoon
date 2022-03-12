import sys


def hanoi(n, start, to, aux):
    if n == 1:
        print(start, to)
        return

    # 원반 n-1개를 aux로 이동
    hanoi(n-1, start, aux, to)

    # 가장 큰 원반 to로 이동
    print(start, to)

    # aux에 있는 n-1개 to로 이동
    hanoi(n-1, aux, to, start)


N = int(sys.stdin.readline())

print(2**N-1)
hanoi(N, 1, 3, 2)