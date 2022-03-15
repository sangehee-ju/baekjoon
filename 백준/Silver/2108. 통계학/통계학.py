import sys
from collections import Counter

N = int(sys.stdin.readline())
ls = []
s = 0
for _ in range(N):
    num = int(sys.stdin.readline())
    ls.append(num)

print(round(sum(ls) / N))

ls.sort()
print(ls[N // 2])

cnt = Counter(ls).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(ls)-min(ls))