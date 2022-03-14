import sys

N = int(sys.stdin.readline())

cnt = 0
find = 666

while True:
    if str(find).find('666') != -1:
        cnt += 1

    if cnt == N:
        print(find)
        break

    find += 1

