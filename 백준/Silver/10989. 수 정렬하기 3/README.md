# [Silver V] 수 정렬하기 3 - 10989 

[문제 링크](https://www.acmicpc.net/problem/10989) 

### 성능 요약

메모리: 30864 KB, 시간: 9896 ms

### date
2022-03-15

### 분류

정렬(sorting)

### 문제 설명

<p>N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.</p>

### 출력 

 <p>첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.</p>


### 처음 풀이 - 모든 입력에 배열을 사용한 counting_sort
```
import sys
# counting sort / time_complexity: O(n)
N = int(sys.stdin.readline())

input_array = [0] * (N + 1)

for n in range(1, N + 1):
    input_array[n] = int(sys.stdin.readline())

# 1) counting_array에 원소들의 빈도값 저장하기
m = max(input_array)
counting_arr = [0] * (m + 1)

for i in input_array:
    counting_arr[i] += 1

# 2) counting_array의 각 요소값에 직전 요소값을 더해 update
s = 0
for i in range(m):
    counting_arr[i+1] += counting_arr[i]

# 3) input_arr를 정렬해 담을 output_arr 선언
output_arr = [-1] * len(input_array)

# 4) 역순으로 input arr 요솟값 output_arr 추가
for i in input_array:
    output_arr[counting_arr[i]-1] = i
    counting_arr[i] -= 1

# 출력
for i in range(1, len(output_arr)):
    print(output_arr[i])
```
---> 메모리 초과 발생

[링크 : ](https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-10989-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python)
코드 참고 후, 메모리를 최대한 확보하고 배열 사용 빈도를 줄여 메모리 초과 문제 해결

