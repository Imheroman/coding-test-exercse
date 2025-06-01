# [16236번: 아기 상어](https://www.acmicpc.net/problem/16236)

N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.

아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.

아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다. 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그
물고기가 있는 칸은 지나갈 수 있다.

아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.

- 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
  - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다.
  - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다. 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은
    빈 칸이 된다.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.

공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.

둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.

- 0: 빈 칸
- 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
- 9: 아기 상어의 위치

아기 상어는 공간에 한 마리 있다.

### 출력

첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.

## 예제

### 예제 입력 1

```text
3
0 0 0
0 0 0
0 9 0
```

### 예제 출력 1

```text
0
```

### 예제 입력 2

```text
3
0 0 1
0 0 0
0 9 0
```

### 예제 출력 2

```text
3
```

### 예제 입력 3

```text
4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
```

### 예제 출력 3

```text
14
```

### 예제 입력 4

```text
6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
```

### 예제 출력 4

```text
60
```

### 예제 입력 5

```text
6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
```

### 예제 출력 5

```text
48
```

### 예제 입력 6

```text
6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
```

### 예제 출력 6

```text
39
```

## 알고리즘 분류

- 구현
- 그래프 이론
- 그래프 탐색
- 시뮬레이션
- 너비 우선 탐색

## 시도

### 시도1(오답)

주어진 조건에 맞춰 아기 상어가 먹을 수 있는 모든 먹이를 먹는데 시간이 얼마나 걸리는지 알아내는 문제이다.

구현은 다 했으나, `check_distance()`에서 거리를 구하는 공식이 잘못됐었다.

단순히 `x, y` 좌표를 이용해서 거리를 구하는게 아니라, 자신보다 큰 물고기는 못 지나가기 떄문에 지나온 거리들을 count 해야 한다.

일단 오답

```python
import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e10)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find(arr, n, current, level, visited):
    x, y = INF, INF

    need_visited = deque([current])
    while need_visited:
        current_x, current_y = need_visited.popleft()

        for dx, dy in DIRECTIONS:
            row, col = current_x + dx, current_y + dy

            if 0 <= row < n and 0 <= col < n and level >= arr[row][col] and visited[row][col] == 0:
                visited[row][col] = visited[current_x][current_y] + 1
                need_visited.append((row, col))

                if arr[row][col] != 0 and level > arr[row][col] and check_distance(current, (x, y), (row, col)):
                    if x >= row and y >= col:
                        x, y = row, col

                    if x > row:
                        x, y = row, col

    if x == INF or y == INF:
        return INF, x, y
    else:
        return visited[x][y], x, y


def check_distance(current, origin, new_position):
    origin_x, origin_y = origin
    new_x, new_y = new_position

    return abs(current[0] - origin_x) + abs(current[1] - origin_y) >= abs(current[0] - new_x) + abs(
        current[1] - new_y)


N = int(input())
graphs = [[] for _ in range(N)]
now = (INF, INF)

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        graphs[i].append(line[j])
        if line[j] == 9:
            now = (i, j)
            graphs[i][j] = 0

level = 2
count = 0
time = 0
while True:
    if count == level:
        count = 0
        level += 1

    visited = [[0] * N for _ in range(N)]
    distance, next_x, next_y = find(graphs, N, now, level, visited)
    count += 1
    if (next_x, next_y) == (INF, INF):
        print(time)
        break

    graphs[next_x][next_y] = 0
    time += distance
    now = (next_x, next_y)
```

### 시도2(35068kb, 136ms - Python3)

distance를 다시 만들 순 있겠지만, 귀찮아서 그냥 visited를 이용해서 해결하였다.

```python
# https://www.acmicpc.net/problem/16236
# 아기 상어
import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e10)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find(arr, n, current, level, visited):
    x, y = INF, INF
    visited[current[0]][current[1]] = 0

    need_visited = deque([current])
    while need_visited:
        current_x, current_y = need_visited.popleft()

        for dx, dy in DIRECTIONS:
            row, col = current_x + dx, current_y + dy

            if 0 <= row < n and 0 <= col < n and level >= arr[row][col] and visited[row][col] == 0:
                visited[row][col] = visited[current_x][current_y] + 1
                need_visited.append((row, col))

                if arr[row][col] != 0 and level > arr[row][col]:
                    if (x, y) == (INF, INF):
                        x, y = row, col
                    if visited[x][y] >= visited[row][col]:
                        if x >= row and y >= col:
                            x, y = row, col

                        if x > row:
                            x, y = row, col

    if x == INF or y == INF:
        return INF, x, y
    else:
        return visited[x][y], x, y


N = int(input())
graphs = [[] for _ in range(N)]
now = (INF, INF)

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        graphs[i].append(line[j])
        if line[j] == 9:
            now = (i, j)
            graphs[i][j] = 0

level = 2
count = 0
time = 0
while True:
    if count == level:
        count = 0
        level += 1

    visited = [[0] * N for _ in range(N)]
    distance, next_x, next_y = find(graphs, N, now, level, visited)
    count += 1
    if (next_x, next_y) == (INF, INF):
        print(time)
        break

    graphs[next_x][next_y] = 0
    time += distance
    now = (next_x, next_y)
```