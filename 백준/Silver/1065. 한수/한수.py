n = int(input())
cnt = 0

for i in range(1, n+1):
    if i < 100:
        cnt += 1
    elif i < 1000:
        d = ((i//10) % 10) - (i//100)
        m = (i//100) + 2*d
        o = i % 10
        if m == o:
            cnt += 1
print(cnt)