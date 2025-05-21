# https://www.acmicpc.net/problem/2644
# 촌수계산
import sys

input = sys.stdin.readline


def dfs(graph, visited, current, target, count=0):
    if current == target:
        print(count)
        exit()

    for p in graph[current]:
        if not visited[p]:
            visited[p] = True
            dfs(graph, visited, p, target, count + 1)

    return -1


N = int(input())
relationships = [[] * (N + 1) for _ in range(N + 1)]
start, end = map(int, input().split())
M = int(input())

for _ in range(M):
    parent, child = map(int, input().split())
    relationships[parent].append(child)
    relationships[child].append(parent)

print(dfs(relationships, [False] * (N + 1), start, end))
