import sys

N = int(sys.stdin.readline())

people = []
cnt = 0
for _ in range(N):
    age, name = sys.stdin.readline().split()
    cnt += 1
    people.append((int(age), cnt, name))

people.sort()

for i in people:
    print(i[0], i[2])