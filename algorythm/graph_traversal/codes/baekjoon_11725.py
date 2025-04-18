# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graphs = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

answer = [-1] * (N + 1)
queue = deque([1])
while queue:
    current = queue.popleft()
    for value in graphs[current]:
        if answer[value] == -1:
            answer[value] = current
            queue.append(value)

print(graphs)
print(answer)

for val in answer[2:]:
    print(val)
