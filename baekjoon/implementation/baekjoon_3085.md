# [3095번: 사탕 게임](https://www.acmicpc.net/problem/3085)

상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다. 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 이제, 모두 같은 색으로
이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 보드의 크기 N이 주어진다. (3 ≤ N ≤ 50)

다음 N개 줄에는 보드에 채워져 있는 사탕의 색상이 주어진다. 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y로 주어진다.

사탕의 색이 다른 인접한 두 칸이 존재하는 입력만 주어진다.

### 출력

첫째 줄에 상근이가 먹을 수 있는 사탕의 최대 개수를 출력한다.

## 예제

### 예제 입력 1

```text
3
CCP
CCP
PPC
```

### 예제 출력 1

```text
3
```

### 예제 입력 2

```text
4
PPPP
CYZY
CCPY
PPCC
```

### 예제 출력 2

```text
4
```

### 예제 입력 3

```text
5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
```

### 예제 출력 3

```text
4
```

## 힌트

예제 3의 경우 4번 행의 Y와 C를 바꾸면 사탕 4개를 먹을 수 있다.

## 알고리즘 분류

- 구현
- 브루트포스 알고리즘

## 시도

### 시도1(시간 초과,, , Python3)

그래프 를 입력 받고, 인접한 위치의 칸의 값이 현재 위치의 칸의 값과 다르면, 위치를 교환하고
행 또는 열에 최대 몇 개의 같은 값이 연속으로 있는지 확인한 후 최댓값을 알아내는 문제이다.

시간 제한이 1초이긴 하지만, N의 크기가 50 이하였기 때문에, 그냥 생각없이 반복문을 사용해도 될 것 같다고 생각했다.

`백트래킹`을 이용하여 값을 교환한 후 원래의 값으로 변경하는 식으로 풀이했다.

백트래킹을 한 이후에는 `bfs`(또는 `dfs`를 이용할 수도 있지만, 일단 bfs가 생각하기 쉬워 보였음)를 이용하여 행 또는 열의 최댓값을 구해주었다.

하지만, 너무 시간 관리를 안 한 나머지 시간 초과 ,,

```python
# https://www.acmicpc.net/problem/3085
# 사탕 게임
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]


# N = 3
# candies = [
#     list("CCP"),
#     list("CCP"),
#     list("PPC")
# ]


def back_tracking(arr, n, size):
    if size == 0:
        # print("=" * 80)
        # for graph in arr:
        #     print(*graph, sep='')

        result = 0
        visited = [[False] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if not visited[r][c]:
                    count = bfs(arr, visited, (r, c), n)
                    result = max(result, count)
        return result

    answer = 0
    for nx in range(n):
        for ny in range(n):
            for dx, dy in DIRECTIONS:
                row, col = nx + dx, ny + dy
                if 0 <= row < n and 0 <= col < n and arr[nx][ny] != arr[row][col]:  # 현재 값과 인접한 값이 다른 값이면
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 교환
                    answer = max(answer, back_tracking(arr, n, size - 1))
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 재교환하여 원래 값으로 변경

    return answer


# def dfs(arr, current, n, color, count):
#     x, y = current
#     if arr[x][y] != color:
#         return count
#
#     if (x == 0 or y == 0) or (x == n - 1 or y == n - 1):
#         return count + 1
#
#     return max(dfs(arr, (x + 1, y), n, color, count + 1) + dfs(arr, (x - 1, y), n, color, count + 1),
#                dfs(arr, (x, y + 1), n, color, count + 1) + dfs(arr, (x, y - 1), n, color, count + 1))


def bfs(arr, visited, current, n):
    cx, cy = current
    visited[cx][cy] = True
    result = 0

    for directions in [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]:
        count = 1
        v = [[False] * n for _ in range(n)]
        v[cx][cy] = True
        need_visited = deque([current])
        while need_visited:
            x, y = need_visited.popleft()

            for dx, dy in directions:
                row, col = x + dx, y + dy
                if 0 <= row < n and 0 <= col < n and not v[row][col] and arr[row][col] == arr[x][y]:
                    visited[row][col] = True
                    v[row][col] = True
                    need_visited.append((row, col))
                    count += 1
        result = max(result, count)
    return result


print(back_tracking(candies, N, 1))
```

### 시도2(35016kb, 3620ms, Python3 - 114884kb, 764ms, Pypy3)

또 어렵게 생각했다.

`bfs`로는 시간을 단축하기 어려울 것 같아서 `dfs`로 접근해보려고 했다.

하지만, 방문했는지 확인하기 위해 계속해서 visited를 생성해줘야했고,
굳이 이렇게 할 필요가 없다고 생각했다.

dfs를 구현하며 생긴 에러를 지피티에게 물어봤는데, 그냥 간단하게 해결하는게 나을 것 같다고 해서 어렵게 생각하지 않고 그냥 간단하게 직접 전체를 순회하며 해결

```python
# https://www.acmicpc.net/problem/3085
# 사탕 게임
import sys
from collections import deque

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ROW = 0
COL = 1

N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]


def back_tracking(arr, n, size):
    if size == 0:
        result = 0
        for i in range(n):
            count = [1, 1]
            for j in range(1, n):
                if arr[i][j] == arr[i][j - 1]:
                    count[ROW] += 1
                    result = max(count[ROW], result)
                if arr[i][j] != arr[i][j - 1]:
                    count[ROW] = 1

                if arr[j][i] == arr[j - 1][i]:
                    count[COL] += 1
                    result = max(count[COL], result)
                if arr[j][i] != arr[j - 1][i]:
                    count[COL] = 1

        return result

    answer = 0
    for nx in range(n):
        for ny in range(n):
            for dx, dy in DIRECTIONS:
                row, col = nx + dx, ny + dy
                if 0 <= row < n and 0 <= col < n and arr[nx][ny] != arr[row][col]:  # 현재 값과 인접한 값이 다른 값이면
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 교환
                    answer = max(answer, back_tracking(arr, n, size - 1))
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 재교환하여 원래 값으로 변경

    return answer


print(back_tracking(candies, N, 1))
```

### 시도3(시간 초과, Pypy3)

오기 생겨서 `dfs`로도 해봤는데 시간 초과,,

지피티 코드대로 하면 `n^4`으로 끝낼 수 있지만, dfs까지 들어가면 최악 `n^5`가 걸리기 때문에
시간 초과가 발생하는 것 같다.

```python
# https://www.acmicpc.net/problem/3085
# 사탕 게임
import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ROW = 0
COL = 1

N = int(input())
candies = [list(input().rstrip()) for _ in range(N)]


def dfs(arr, n, current, direction, color):
    x, y = current
    dx, dy = direction
    row, col = x + dx, y + dy
    if 0 <= row < n and 0 <= col < n and arr[row][col] == color:
        return 1 + dfs(arr, n, (row, col), direction, color)
    return 0


def back_tracking(arr, n, size):
    if size == 0:
        answer = 0
        for i in range(n):
            for j in range(n):
                result = 0
                for directions in [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]]:
                    count = 0
                    for direction in directions:
                        count += dfs(arr, n, (i, j), direction, arr[i][j])
                    result = max(result, count + 1)
                answer = max(answer, result)
        return answer

    answer = 0
    for nx in range(n):
        for ny in range(n):
            for dx, dy in DIRECTIONS:
                row, col = nx + dx, ny + dy
                if 0 <= row < n and 0 <= col < n and arr[nx][ny] != arr[row][col]:  # 현재 값과 인접한 값이 다른 값이면
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 교환
                    answer = max(answer, back_tracking(arr, n, size - 1))
                    arr[nx][ny], arr[row][col] = arr[row][col], arr[nx][ny]  # 재교환하여 원래 값으로 변경

    return answer


print(back_tracking(candies, N, 1))
```

## 정리 및 소감

쓸데 없는 알고리즘 구현보다 일반 구현으로 할 때가 더 나을 때도 있다.
