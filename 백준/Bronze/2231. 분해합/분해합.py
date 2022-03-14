import sys

# 분해합 입력받기
N = int(sys.stdin.readline())

res = 0
# 1부터 N까지의 수 중 분해합 N의 생성자 찾기
for i in range(1, N+1):
    # i의 각 자리수 담기
    A = list(map(int, str(i)))
    
    # res : i의 분해합
    res = i + sum(A)
    
    # res와 N이 같으면, i는 N의 생성자
    if res == N:
        print(i)
        break
    
    # i가 N과 같아지면, N의 생성자는 없는 것
    if i == N:
        print(0)
        