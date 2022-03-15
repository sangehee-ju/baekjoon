# [Silver II] 좌표 압축 - 18870 

[문제 링크](https://www.acmicpc.net/problem/18870) 

### 성능 요약

메모리: 144088 KB, 시간: 2096 ms

### 날짜
2022-03-16

### 분류

값 / 좌표 압축(coordinate_compression), 정렬(sorting)

### 문제 설명

<p>수직선 위에 N개의 좌표 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.</p>

<p>X<sub>i</sub>를 좌표 압축한 결과 X'<sub>i</sub>의 값은 X<sub>i</sub> > X<sub>j</sub>를 만족하는 서로 다른 좌표의 개수와 같아야 한다.</p>

<p>X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>에 좌표 압축을 적용한 결과 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>를 출력해보자.</p>

### 입력 

 <p>첫째 줄에 N이 주어진다.</p>

<p>둘째 줄에는 공백 한 칸으로 구분된 X<sub>1</sub>, X<sub>2</sub>, ..., X<sub>N</sub>이 주어진다.</p>

### 출력 

 <p>첫째 줄에 X'<sub>1</sub>, X'<sub>2</sub>, ..., X'<sub>N</sub>을 공백 한 칸으로 구분해서 출력한다.</p>

### 시간 초과였던 코드
```
# 시간초과
import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
freq = []

# 개수 확인을 위해 유일한 원소만 담긴 set 선언
check = set(nums)

# ==> 비교
for i in check:
    cnt = 0
    for j in check:
        if i > j:
            cnt += 1
    freq.append((i, cnt))

for i in nums:
    for j in freq:
        if i == j[0]:
            print(j[1], end=' ')
```

