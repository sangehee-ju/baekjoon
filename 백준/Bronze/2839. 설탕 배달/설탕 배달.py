N = int(input())

cnt = 0

while N >= 0:
    # 5의 배수이면, 바로 개수 세기
    if N % 5 == 0:
        cnt += int(N // 5)
        print(cnt)
        break
    # 5의 배수가 아니면, 계속해서 3 빼기
    N -= 3
    cnt += 1
else:
    print(-1)
