# https://www.acmicpc.net/problem/5014
# 스타트링크

import sys
from collections import deque

input = sys.stdin.readline

size, start, end, up, down = map(int, input().split())
# size, start, end, up, down = 10, 1, 10, 2, 1
# size, start, end, up, down = 100, 2, 1, 1, 0
# size, start, end, up, down = 547014, 339337, 103757, 456334, 12855  # 287262
# size, start, end, up, down = 838479, 582568, 628084, 58889, 670667  # 265304

need_visited = deque([start])
visited = [0] * (size + 1)
visited[start] = 1
while need_visited:
    now = need_visited.popleft()

    if now == end:
        print(visited[end] - 1)
        break

    for post in [up, -down]:
        _next = now + post
        if 0 <= _next <= size and visited[_next] == 0:
            need_visited.append(_next)
            visited[_next] = visited[now] + 1
else:
    print("use the stairs")