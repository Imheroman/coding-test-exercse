# [2573번: 빙산]()

지구 온난화로 인하여 북극의 빙산이 녹고 있다. 빙산을 그림 1과 같이 2차원 배열에 표시한다고 하자. 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장된다. 빙산 이외의 바다에 해당되는 칸에는 0이
저장된다. 그림 1에서 빈칸은 모두 0으로 채워져 있다고 생각한다.

|   |   |   |   |   |   | |
|---|---|---|---|---|---|-|
|   | 2 | 4 | 5 | 3 |   | |
|   | 3 |   | 2 | 5 | 2 |
|   | 7 | 6 | 2 | 4 |
|   |   |   |   |   |   | |

그림 1. 행의 개수가 5이고 열의 개수가 7인 2차원 배열에 저장된 빙산의 높이 정보

빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 줄어들기 때문에, 배열에서 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다. 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다. 따라서 그림 1의 빙산은 일년후에 그림 2와 같이 변형된다.

그림 3은 그림 1의 빙산이 2년 후에 변한 모습을 보여준다. 2차원 배열에서 동서남북 방향으로 붙어있는 칸들은 서로 연결되어 있다고 말한다. 따라서 그림 2의 빙산은 한 덩어리이지만, 그림 3의 빙산은 세 덩어리로
분리되어 있다.

|   |   |   |   |   | | |
|---|---|---|---|---|-|-|
|   |   | 2 | 4 | 1 | | |
|   | 1 |   | 1 | 5 | | |
|   | 5 | 4 | 1 | 2 | | |
|   |   |   |   |   | | |

그림 2

|   |   |   |   |   | | |
|---|---|---|---|---|-|-|
|   |   | 3 |   |   | | |
|   |   |   | 4 |   | | |
|   | 3 | 2 |   |   | | |
|   |   |   |   |   | | |

그림 3

한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하는 프로그램을 작성하시오. 그림 1의 빙산에 대해서는 2가 답이다. 만일 전부 다 녹을 때까지 두 덩어리 이상으로
분리되지 않으면 프로그램은 0을 출력한다.

## 입출력

### 입력

첫 줄에는 이차원 배열의 행의 개수와 열의 개수를 나타내는 두 정수 N과 M이 한 개의 빈칸을 사이에 두고 주어진다. N과 M은 3 이상 300 이하이다. 그 다음 N개의 줄에는 각 줄마다 배열의 각 행을 나타내는
M개의 정수가 한 개의 빈 칸을 사이에 두고 주어진다. 각 칸에 들어가는 값은 0 이상 10 이하이다. 배열에서 빙산이 차지하는 칸의 개수, 즉, 1 이상의 정수가 들어가는 칸의 개수는 10,000 개 이하이다.
배열의 첫 번째 행과 열, 마지막 행과 열에는 항상 0으로 채워진다.

### 출력

첫 줄에 빙산이 분리되는 최초의 시간(년)을 출력한다. 만일 빙산이 다 녹을 때까지 분리되지 않으면 0을 출력한다.

## 예제

### 예제 입력 1

```text
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
```

### 예제 출력 1

```text
2
```

## 알고리즘 분류

- 구현
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 시도

### 시도1(오답, Python 3)

주변에 0인 인접한 바다를 찾아서 빙산의 크기를 줄이고, 2덩어리로 분리됐을 때 걸린 시간을 구하는 문제이다.

조금 고민을 해봤으나, 첫 시도는 그냥 모든 경우의 수를 직접 구현하여 문제를 해결하는 것으로 결정했다.

1. 2덩어리 이상으로 분리됐는지 확인한다.
2. 2덩이리 이상으로 분리되지 않았다면,
   그래프를 돌다가 현재 값이 0이 아닌 경우 4방면을 방문해서 0인 곳의 횟수 만큼 현재 값을 감소시킨다.
1. 그런데, 현재값이 0이 바로 돼버리면 주변 좌표를 방문했을 시 현재의 값도 바다로 인식하는 경우가 생긴다.
2. 따라서 `visit`를 이용해서 방금 바다가 되었다고 표시를 해준다.

이 생각한 알고리즘이고, 이에 맞춰 코드를 작성했다.

하지만, 오답 ,,

```python
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


def melting_ice(arr, v, start):
    current_x, current_y = start
    count = 0
    for dx, dy in DIRECTIONS:
        row, col = current_x + dx, current_y + dy

        if 0 <= row < N and 0 <= col < M:
            if not v[row][col] and arr[row][col] == 0:
                count += 1
    return count


def count_block(arr, v):
    v[i][j] = True
    need_visited = deque([(i, j)])
    while need_visited:
        current_x, current_y = need_visited.popleft()
        for x, y in DIRECTIONS:
            r, c = current_x + x, current_y + y
            if 0 <= r < N and 0 <= c < M and arr[r][c] > 0 and not v[r][c]:
                v[r][c] = True
                need_visited.append((r, c))
    return


for year in range(11):
    result = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] != 0 and not visit[i][j]:
                count_block(graphs, visit)
                result += 1

    if result > 1:
        print(year)
        exit()
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] != 0:
                visited[i][j] = True
                graphs[i][j] = max(0, graphs[i][j] - melting_ice(graphs, visited, (i, j)))

print(0)
```

### 시도2(시간 초과, Python 3)

1번 시도해본 후 인터넷에 검색해본 반례도 모두 알맞게 나와서 `맞왜틀`이라고 고민을 했었다.

다른 블로그를 참고해 봐도, 다른 블로그는 `while True:`로 시작하는 것 외에 크게 다른 점이 없다고 생각했고, 더 시간을 쓰는 것 보단 무엇이 문제인지 파악하기 위해 지피티에게 이유를 물어봤다.

지피티는 아래와 같은 답을 줬다.

```python
for year in range(10000):  # 충분히 큰 수
```

나는 문제에서 분명 10보다 작은 수라고 해서 11회만 돌도록 설정을 했는데, 왜 충분히 큰 수가 들어가야 하나 질문했다.

![스크린샷 2025-05-28 오전 1.25.23.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fj4%2Flffybpwx1j7f046vfs9dpx9r0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_T3k36N%2F%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202025-05-28%20%EC%98%A4%EC%A0%84%201.25.23.png)

이라고 답변을 했고, 곰곰히 다시 생각을 해더니,

(대충 생각해본 극단적 예시)

```text
0 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10
10 10 10 10 10 10 10 10
```

이런 느낌으로 빙산이 있으면, 당연히 약 10년 안에는 해결이 될 리가 없었다.

이후 반복문을 큰 수로 설정한 코드

하지만, 시간 초과 발생

```python
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


def melting_ice(arr, v, start):
    current_x, current_y = start
    count = 0
    for dx, dy in DIRECTIONS:
        row, col = current_x + dx, current_y + dy

        if 0 <= row < N and 0 <= col < M:
            if not v[row][col] and arr[row][col] == 0:
                count += 1
    return count


def count_block(arr, v):
    v[i][j] = True
    need_visited = deque([(i, j)])
    while need_visited:
        current_x, current_y = need_visited.popleft()
        for x, y in DIRECTIONS:
            r, c = current_x + x, current_y + y
            if 0 <= r < N and 0 <= c < M and arr[r][c] > 0 and not v[r][c]:
                v[r][c] = True
                need_visited.append((r, c))
    return


for year in range(100000):
    result = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] != 0 and not visit[i][j]:
                count_block(graphs, visit)
                result += 1

    if result > 1:
        print(year)
        exit()
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] != 0:
                visited[i][j] = True
                graphs[i][j] = max(0, graphs[i][j] - melting_ice(graphs, visited, (i, j)))

print(0)
```

### 시도3(218848kb, 888ms, Pypy3)

시간 초과가 발생해서 시도2와 똑같은 코드에 pypy3로 제출을 해봤더니 역시 시간 초과가 발생했다.

`year`을 반복하는 범위가 너무 커서 그래프의 범위가 커졌을 때의 반복 시간을 감당하지 못 하는 것 같았다.

결국, `result`가 0인 경우(모두 0인 경우 = 빙산이 존재하지 않는 경우)일 때 break를 했고,
pypy3로 제출하니 일단 문제 해결하여 만족 !

```python
# https://www.acmicpc.net/problem/2573
# 빙산
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N, M = map(int, input().split())
graphs = [list(map(int, input().split())) for _ in range(N)]


def melting_ice(arr, v, start):
    current_x, current_y = start
    count = 0
    for dx, dy in DIRECTIONS:
        row, col = current_x + dx, current_y + dy

        if 0 <= row < N and 0 <= col < M:
            if not v[row][col] and arr[row][col] == 0:
                count += 1
    return count


def count_block(arr, v):
    v[i][j] = True
    need_visited = deque([(i, j)])
    while need_visited:
        current_x, current_y = need_visited.popleft()
        for x, y in DIRECTIONS:
            r, c = current_x + x, current_y + y
            if 0 <= r < N and 0 <= c < M and arr[r][c] > 0 and not v[r][c]:
                v[r][c] = True
                need_visited.append((r, c))
    return


for year in range(100000):
    result = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graphs[i][j] != 0 and not visit[i][j]:
                count_block(graphs, visit)
                result += 1

    if result > 1:
        print(year)
        exit()
    elif result == 0:
        print(0)
        exit()
    visited = [[False] * M for _ in range(N)]
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if graphs[i][j] != 0:
                visited[i][j] = True
                graphs[i][j] = max(0, graphs[i][j] - melting_ice(graphs, visited, (i, j)))

print(0)
```