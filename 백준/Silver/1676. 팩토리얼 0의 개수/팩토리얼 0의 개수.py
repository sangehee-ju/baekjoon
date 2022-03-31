import sys

N = int(sys.stdin.readline())

facto = 1

for i in range(N, 0, -1):
    facto *= i

cnt = 0
while True:
    if facto % 10 != 0:
        break

    cnt += 1
    facto //= 10

print(cnt)