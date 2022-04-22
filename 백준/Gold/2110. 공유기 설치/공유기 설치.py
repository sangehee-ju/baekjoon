import sys

r = sys.stdin.readline

n, c = map(int, r().split())
coord = [int(r()) for _ in range(n)]
coord.sort()


def binarySearch(arr, start, end):
    while start <= end:
        mid = (start + end) // 2
        cur = arr[0]
        cnt = 1

        for i in range(1, len(arr)):
            if arr[i] >= cur + mid:
                cnt += 1
                cur = arr[i]

        if cnt >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


start, end = 1, coord[-1] - coord[0]  # 시작 : 최소 거리, 끝 : 최대 거리
answer = 0

binarySearch(coord, start, end)
print(answer)
