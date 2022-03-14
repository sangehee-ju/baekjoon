T = int(input())

for _ in range(T):
    h, w, n = map(int, input().split())
    YY = n % h
    XXX = n // h + 1
    if n % h == 0:
        YY = h
        XXX = n//h

    print(YY*100+XXX)
