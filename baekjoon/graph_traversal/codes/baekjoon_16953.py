# https://www.acmicpc.net/problem/16953
# A -> B
import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
# a, b = 2, 162
# a, b = 4, 42
# a, b = 100, 40021
visited = [False] * (b + 1)
need_visited = deque([(1, a)])
while need_visited:
    count, current = need_visited.popleft()

    if current == b:
        print(count)
        exit()

    for n in [int(str(current) + "1"), current * 2]:
        if n <= b and not visited[n]:
            need_visited.append((count + 1, n))
            visited[n] = True

print(-1)