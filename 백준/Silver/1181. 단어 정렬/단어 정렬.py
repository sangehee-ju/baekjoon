import sys

N = int(sys.stdin.readline())

words = []
length = []

for _ in range(N):
    words.append(sys.stdin.readline().replace('\n', ''))

# words list => set : list 내 중복된 원소 제거
words = set(words)

# (길이, 단어) 튜플 형태로 저장
for i in words:
    length.append((len(i), i))

# 길이에 따라 정렬 > 사전 순으로 정렬 하는 sort의 성질이용.
length.sort()

for i in length:
    print(i[1])

