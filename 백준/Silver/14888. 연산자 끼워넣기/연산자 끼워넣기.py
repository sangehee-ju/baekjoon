import sys

r = sys.stdin.readline
N = int(r())

nums = list(map(int, r().split()))
plus, sub, multi, divide = map(int, r().split())

res = []

max_value = -1e9
min_value = 1e9


def dfs(i, arr):
    global plus, sub, multi, divide, max_value, min_value
    if i == N:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)
    else:
        if plus > 0:
            plus -= 1
            dfs(i + 1, arr + nums[i])
            plus += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, arr - nums[i])
            sub += 1
        if multi > 0:
            multi -= 1
            dfs(i + 1, arr * nums[i])
            multi += 1
        if divide > 0:
            divide -= 1
            dfs(i + 1, int(arr / nums[i]))
            divide += 1


dfs(1, nums[0])

print(max_value)
print(min_value)
