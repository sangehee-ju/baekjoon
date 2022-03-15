import sys

N = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
arr = list(sorted(set(nums)))

dic = {arr[i]: i for i in range(len(arr))}

for i in nums:
    print(dic[i], end=' ')

