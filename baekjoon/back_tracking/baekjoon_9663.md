# [9663번: N-Queen](https://www.acmicpc.net/problem/9663)

N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 N이 주어진다. (1 ≤ N < 15)

### 출력

첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

## 예제

### 예제 입력 1

```text
8
```

### 예제 출력 1

```text
92
```

## 알고리즘 분류

- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(시간 초과 - PyPy3)

N X N의 보드에 서로 공격할 수 없는 N개의 퀸을 놓을 수 있는 경우의 수가 몇 개인지 알아내는 문제이다.

시도해본 문제 해결법은

1. 백트래킹을 이용하여 이동할 수 있는 모든 좌표를 저장한다.
2. 8개의 좌표가 모였을 때, 퀸의 이동 경로를 `visited`를 이용하여 표시하고
3. 이미 방문한 좌표에 퀸을 놓아야한다면 0을 return하고
4. 모두 놓아진 경우 1을 return하여 모든 경우의 수를 더한다.

```python
import sys
from collections import deque

input = sys.stdin.readline

EIGHT_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]


def back_tracking(n, size, repository):
    if size == 0:
        visited = [[False] * n for _ in range(n)]
        for x, y in repository:
            if visited[x][y]:
                return 0

            for dx, dy in EIGHT_DIRECTIONS:
                row, col = x, y
                while 0 <= row < n and 0 <= col < n:
                    visited[row][col] = True
                    row, col = row + dx, col + dy
        return 1

    result = 0
    for i in range(n):
        for j in range(n):
            if (i, j) not in repository:
                repository.append((i, j))
                result += back_tracking(n, size - 1, repository)
                repository.pop()

    return result


N = int(input())
answer = 0
print(back_tracking(N, N, deque([])))
```

### 시도2(209684kb, 29120ms - PyPy3 / 시간 초과 - Python3)

[Stranger's LAB](https://st-lab.tistory.com/118)님의 블로그를 보고 작성한 코드이다.

여러번 봐도 직접 좌표를 찍어보고 비교하는 것 밖에 구현할 수 없을 것 같아서 구글에 검색해봤다.

**Stranger's LAB**님은 방문 위치를 1차원 배열로 관리했다.

1차원 배열의 `index`를 `row`로 지정하고, 해당 `row`에 `column`을 한 개씩 방문하여 더 방문할 수 있는지 확인한다.

확인한 후 방문할 수 있다면(다른 퀸의 공격을 받는 영역이 아니라면) 다음 퀸으로 이동한다.

여기에서 다른 퀸의 공격을 받는지 확인하는 2가지 조건이 있는데 조건 부분이 이해하기 어려웠다.

```python
def is_available(arr, row):
    for r in range(row):
        if (arr[row] == arr[r]) or (abs(row - r) == abs(arr[row] - arr[r])):
            return False

    return True
```

위 코드에서 작성된 조건 중

1. `arr[row] == arr[r]` 이 코드는 비교적 이해하기 쉬웠는데, 같은 열이 저장된 행이 있는지 확인하는 부분이다. (열이 같으면 다른 퀸이 공격할 수 있기 때문이다.)
  + `row` 별로 배열에 저장중이기 때문에 `row`가 겹칠 일은 없다.
2. `abs(row - r) == abs(arr[row] - arr[r])` 이 코드의 의미는 이해하기가 어려웠다.(아직도 정확하게 이해는 안 됐다 ,,)
  + `abs(row - r)` 코드는 두 row 사이의 거리를 구한다.
  + `abs(arr[row] - arr[r])` 코드는 두 col 사이의 거리를 구한다.
  + 대각선은 행 간 거리 == 열 간 거리일 때 존재하기 때문에 값이 동일하다면 `False`를 return 한다.

```python
# https://www.acmicpc.net/problem/9663
# N-Queen
# 참고 블로그: https://st-lab.tistory.com/118
import sys

input = sys.stdin.readline


def is_available(arr, row):
    for r in range(row):
        if (arr[row] == arr[r]) or (abs(row - r) == abs(arr[row] - arr[r])):
            return False

    return True


def n_queen(arr, n, row):
    if row == n:
        global answer
        answer += 1
        return

    for col in range(n):
        arr[row] = col

        if is_available(arr, row):
            n_queen(arr, n, row + 1)


N = int(input())
# N = 8
answer = 0
graphs = [0] * N
n_queen(graphs, N, 0)
print(answer)
```