# [10026번: 적록색약](https://www.acmicpc.net/problem/10026)

적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.

크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해
있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)

예를 들어, 그림이 아래와 같은 경우에

```text
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
```

적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)

그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)

둘째 줄부터 N개 줄에는 그림이 주어진다.

### 출력

적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.

## 예제

### 예제 입력 1

```text
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
```

### 예제 출력 1

```text
4 3
```

## 시도

### 시도1(BFS, 84ms)

BFS 풀이

graph를 2개로 나누어 BFS로 색을 구분하여 찾은 후 색이 변경되는 지점마다 count를 한다.

코드 중복이 있지만, 일단 문제 풀이를 중점으로 두었기 때문에 따로 수정하지 않았음

```python
# https://www.acmicpc.net/problem/10026
# 적록색약
from collections import deque
from sys import stdin
import copy

input = stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
# N = 5
# graph = [
#     list("RGRBB"),
#     list("GGBBB"),
#     list("BBBRR"),
#     list("BBRRR"),
#     list("RRRRR")
# ]


def bfs(g, start, color):
    need_visited = deque()
    need_visited.append(start)

    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < N and 0 <= col < N and g[row][col] == color:
                g[row][col] = "X"
                need_visited.append((row, col))


def color_weakness_bfs(g, start, colors):
    need_visited = deque()
    need_visited.append(start)

    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < N and 0 <= col < N and g[row][col] in colors:
                g[row][col] = "X"
                need_visited.append((row, col))


answer = [0, 0]
deepcopy = copy.deepcopy(graph)
for r in range(N):
    for c in range(N):
        if graph[r][c] == "R" or graph[r][c] == "G":
            color_weakness_bfs(graph, (r, c), ["R", "G"])
            answer[1] += 1
        elif graph[r][c] == "B":
            color_weakness_bfs(graph, (r, c), ["B"])
            answer[1] += 1
        if deepcopy[r][c] == "R" or deepcopy[r][c] == "B" or deepcopy[r][c] == "G":
            bfs(deepcopy, (r, c), deepcopy[r][c])
            answer[0] += 1

print(*answer, sep=" ")
```

### 시도 2 (DFS, 72ms)

DFS

BFS와 풀이는 똑같지만, DFS 방식의 코드

```python
# https://www.acmicpc.net/problem/10026
# 적록색약
from sys import stdin
import sys
import copy

sys.setrecursionlimit(10 ** 6)
input = stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
# N = 5
# graph = [
#     list("RGRBB"),
#     list("GGBBB"),
#     list("BBBRR"),
#     list("BBRRR"),
#     list("RRRRR")
# ]


def dfs(g, start, colors):
    x, y = start
    for dx, dy in DIRECTIONS:
        row, col = x + dx, y + dy
        if 0 <= row < N and 0 <= col < N and g[row][col] in colors:
            g[row][col] = "X"
            dfs(g, (row, col), colors)


answer = [0, 0]
deepcopy = copy.deepcopy(graph)
for r in range(N):
    for c in range(N):
        if graph[r][c] == "R" or graph[r][c] == "G":
            dfs(graph, (r, c), ["R", "G"])
            answer[1] += 1
        elif graph[r][c] == "B":
            dfs(graph, (r, c), ["B"])
            answer[1] += 1
        if deepcopy[r][c] == "R" or deepcopy[r][c] == "B" or deepcopy[r][c] == "G":
            dfs(deepcopy, (r, c), [deepcopy[r][c]])
            answer[0] += 1

print(*answer, sep=" ")
```

## 정리

그래프를 2개 복사하는게 좋은 접근 방법은 아닐 것 같아서 다른 방법이 있나 블로그를 참고해 보았지만, 
다 비슷한 것 같다.

단순히 BFS, DFS를 구현할 줄 알고, 문제를 이해할 수 있으면 풀 수 있는 문제같다.
