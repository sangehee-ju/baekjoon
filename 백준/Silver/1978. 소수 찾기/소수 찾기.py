N = int(input())

nums = list(map(int, input().split()))
cnt = 0

for i in nums:
    p = True
    for j in range(2, i):
        while i % j == 0:
            if j == i:
                i /= j
                continue
            i /= j
            p = False
    if p:
        if i != 1:
            cnt += 1

print(cnt)
