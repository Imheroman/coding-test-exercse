# [2206번: 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)

N×M의 행렬로 표현되는 맵이 있다. 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳을 나타낸다. 당신은 (1, 1)에서 (N, M)의 위치까지 이동하려 하는데, 이때 최단 경로로 이동하려 한다. 최단경로는 맵에서 가장 적은 개수의 칸을 지나는 경로를 말하는데, 이때 시작하는 칸과 끝나는 칸도 포함해서 센다.

만약에 이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.

한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.

맵이 주어졌을 때, 최단 경로를 구해 내는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 1,000)이 주어진다. 다음 N개의 줄에 M개의 숫자로 맵이 주어진다. (1, 1)과 (N, M)은 항상 0이라고 가정하자.

### 출력

첫째 줄에 최단 거리를 출력한다. 불가능할 때는 -1을 출력한다.

## 예제

### 예제 입력 1

```text
6 4
0100
1110
1000
0000
0111
0000
```

### 예제 출력 1

```text
15
```

### 예제 입력 2

```text
4 4
0111
1111
1111
1110
```

### 예제 출력 2

```text
-1
```

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 격자 그래프

## 시도

### 시도1(시간 초과)

`0, 0`에서 `n-1, m-1`까지 도달하는데, 가장 최소한의 거리로 이동하며, 벽은 최대 1개까지 부수며 이동하는 문제이다.

모든 좌표에 1을 1개씩 제거해서 탐색을 해봤는데 시간 초과가 발생했다.  

```python
# https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e10)

N, M = map(int, input().split())
graphs = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# N, M = 6, 4
# graphs = [
#     list(map(int, list("0100"))),
#     list(map(int, list("1110"))),
#     list(map(int, list("1000"))),
#     list(map(int, list("0000"))),
#     list(map(int, list("0111"))),
#     list(map(int, list("0000"))),
# ]


def bfs(graph, n, m, size):
    if size == 0:  # bfs 코드
        
        visited = [[0] * M for _ in range(N)]
        visited[0][0] = 1
        need_visited = deque([(0, 0)])
        while need_visited:
            r, c = need_visited.pop()

            for dx, dy in DIRECTIONS:
                row, col = r + dx, c + dy

                if 0 <= row < n and 0 <= col < m and visited[row][col] == 0:
                    if graph[row][col] == 0:
                        visited[row][col] = visited[r][c] + 1
                        need_visited.append((row, col))

        return visited[n - 1][m - 1]

    result = INF
    for i in range(n):
        for j in range(m):
            origin = graph[i][j]  # 원래의 값을 저장해놓고
            graph[i][j] = 0  # 1이든 0이든 일단 벽을 1개 부쉈다고 생각
            res = bfs(graph, n, m, size - 1)
            if res != 0:  # 마지막까지 도달한 경우
                result = min(result, res)
            graph[i][j] = origin  # 원래의 값으로 되돌림

    return result


answer = bfs(graphs, N, M, 1)

if answer == INF:
    print(-1)
else:
    print(answer)
```

### 시도2

```python

```

### 시도3

```python

```

### 시도4

```python

```

## 정리

