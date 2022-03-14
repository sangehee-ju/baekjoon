import sys

N = int(sys.stdin.readline())

# 메모리 미리 확보 -> 메모리 초과 방지
in_arr = [0]*10001

# 숫자 입력 받기
for i in range(N):
    num = int(sys.stdin.readline())
    # in_arr에 빈도 표시
    in_arr[num] += 1

for i in range(10001):
    # i가 입력되었을 때,
    if in_arr[i] != 0:
        # 입력된 i를 빈도수 만큼 출력하기
        for _ in range(in_arr[i]):
            print(i)
