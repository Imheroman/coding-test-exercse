# [1261번: 알고스팟](https://www.acmicpc.net/problem/1261)

알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수
없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을
때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 알고스팟에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 Baekjoon Online Judge에 수록되어 있기 때문에, sudo를
사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을
의미한다.

(1, 1)과 (N, M)은 항상 뚫려있다.

### 출력

첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.

## 예제

### 예제 입력 1

```text
3 3
011
111
110
```

### 예제 출력 1

```text
3
```

### 예제 입력 2

```text
4 2
0001
1000
```

### 예제 출력 2

```text
0
```

### 예제 입력 3

```text
6 6
001111
010000
001111
110001
011010
100010
```

### 예제 출력 3

```text
2
```

## 힌트

- 이 문제는 [알고스팟](https://algospot.com/judge/problem/read/BOJ)에서도 풀 수 있다.

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 최단 경로
- 데이크스트라
- 격자 그래프
- 0-1 너비 우선 탐색

## 시도

### 시도1(34968kb, 68ms)

이전에 [미로 만들기](./baekjoon_2665.md)에서 풀었던 유형과 똑같은 문제라 바로 해당 문제 풀이법이 떠올랐다.

얼마 전에 풀었던 문제라 바로 생각이 났고, `bfs`를 이용해서 문제를 해결했다.

```python
# https://www.acmicpc.net/problem/1261
# 알고스팟
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
graphs = [list(input().rstrip()) for _ in range(N)]
# M, N = 3, 3
# graphs = [['0', '1', '1'], ['1', '1', '1'], ['1', '1', '0']]
# M, N = 4, 2
# graphs = [['0', '0', '0', '1'], ['1', '0', '0', '0']]

visited = [[-1] * M for _ in range(N)]
need_visited = deque([(0, 0)])

visited[0][0] = 0
while need_visited:
    x, y = need_visited.popleft()

    if x == N - 1 and y == M - 1:
        break

    for dx, dy in DIRECTIONS:
        row, col = x + dx, y + dy

        if 0 <= row < N and 0 <= col < M and visited[row][col] == -1:
            if graphs[row][col] == "0":
                visited[row][col] = visited[x][y]
                need_visited.appendleft((row, col))
            else:
                visited[row][col] = visited[x][y] + 1
                need_visited.append((row, col))

print(visited[N - 1][M - 1])
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

