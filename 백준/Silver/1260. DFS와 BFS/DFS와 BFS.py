import sys
from collections import deque


def dfs(graph, root):
    stack = [root]
    visit = []

    while stack:
        n = stack.pop()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visit)


def bfs(graph, root):
    queue = deque([root])
    visit = []

    while queue:
        n = queue.popleft()
        if n not in visit:
            visit.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visit))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visit)


r = sys.stdin.readline

N, M, V = map(int, r().split())

graph = {}

for i in range(M):
    start, end = map(int, r().split())

    if start not in graph:
        graph[start] = [end]
    elif end not in graph[start]:
        graph[start].append(end)

    if end not in graph:
        graph[end] = [start]
    elif start not in graph[end]:
        graph[end].append(start)

print(dfs(graph, V))
print(bfs(graph, V))
