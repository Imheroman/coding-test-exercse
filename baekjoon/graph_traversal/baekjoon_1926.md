# [1926번: 그림](https://www.acmicpc.net/problem/1926)

어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자.
가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.

## 입출력

### 입력

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다.
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)

### 출력

첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라.
단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.

## 예제

### 예제 입력 1

```text
6 5
1 1 0 1 1
0 1 1 0 0
0 0 0 0 0
1 0 1 1 1
0 0 1 1 1
0 0 1 1 1
```

### 예제 출력 1

```text
4
9
```

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색
- 격자 그래프
- 플러드 필

## 시도

### 시도1(34968kb, 264ms)

전형적인 그래프 탐색 문제라서 쉽게 풀었다.

1인 곳의 위치를 파악해서 크기를 파악하고, 발견한 그래프 수와 가장 큰 크기를 출력한다.

```python
# https://www.acmicpc.net/problem/1926
# 그림
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


def bfs(start):
    size = 1

    need_visited = deque([start])
    while need_visited:
        x, y = need_visited.popleft()
        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy

            if (0 <= row < N and 0 <= col < M) and graphs[row][col] == 1:
                size += 1
                need_visited.append((row, col))
                graphs[row][col] = 0

    return size


count = 0
max_size = 0
for i in range(N):
    for j in range(M):
        if graphs[i][j] == 1:
            count += 1
            graphs[i][j] = 0
            max_size = max(bfs((i, j)), max_size)

print(count)
print(max_size)
```