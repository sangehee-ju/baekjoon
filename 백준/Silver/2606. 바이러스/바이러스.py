import sys


def dfs(graph):
    stack = [1]
    visit = []

    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort(reverse=True)
                stack += temp

    return len(visit) - 1


r = sys.stdin.readline

# 컴퓨터의 수/ <100
N = int(r())

conn = [[] * N for i in range(N + 1)]

# 컴퓨터의 연결 수
con = int(r())

graph = {}
for i in range(con):
    n1, n2 = map(int, r().split())

    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(dfs(graph))
