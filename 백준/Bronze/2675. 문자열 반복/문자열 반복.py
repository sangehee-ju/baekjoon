T = int(input())  # 테스트 케이스

for i in range(T):
    n, s = input().split()

    n = int(n)

    for st in s:
        print(st * n, end='')
    print()
