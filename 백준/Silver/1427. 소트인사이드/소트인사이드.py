import sys

N = list(sys.stdin.readline())

N.remove('\n')

N = list(map(int, N))

N.sort(reverse=True)

N = list(map(str, N))

print(int(''.join(N)))

