import sys

r = sys.stdin.readline

N = int(r())
arr = []

for i in range(N):
    arr.append(list(map(int, r().split())))

k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            arr[i][j] += arr[i - 1][j]
        elif i == j:
            arr[i][j] += arr[i - 1][j - 1]
        else:
            arr[i][j] += max(arr[i - 1][j - 1], arr[i - 1][j])
    k += 1
print(max(arr[N - 1]))
