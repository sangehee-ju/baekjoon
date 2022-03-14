n = int(input())
b = list(map(int, list(input())))
res = 0
for i in range(n):
    res += b[i]
print(res)
