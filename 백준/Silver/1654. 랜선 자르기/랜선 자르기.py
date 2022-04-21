import sys

r = sys.stdin.readline

k, n = map(int, r().split())
line = [int(r()) for _ in range(k)]
start, end = 1, max(line)  # 이분 탐색 위치

while start <= end:
    mid = (start + end) // 2
    lines = 0 #선의 개수
    for i in line:
        lines += i // mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)
