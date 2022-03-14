N = int(input())

cnt = N

for _ in range(N):
    word = input()

    for idx in range(len(word) - 1):
        # idx를 기준으로 앞뒤 단어가 다를 경우
        if word[idx] != word[idx + 1]:
            # idx 뒤쪽 인덱스의 문자열에서 word[idx+1] 문자가 포함되어 있는 지 확인
            if word[idx + 1] in word[:idx]:
                cnt -= 1
                break
print(cnt)
