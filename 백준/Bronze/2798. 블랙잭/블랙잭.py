from itertools import combinations
N, M = input().split(' ')
N = int(N)
M = int(M)
# 입력될 수 들을 담는 리스트 lst
lst = input().split(' ')
lst = list(map(int, lst))
res = list(combinations(lst, 3))
m = 0
for t in res:
    total = 0
    for i in range(len(t)):
        total += t[i]
    if (total <= M) & (m < total):
        m = total
print(m)