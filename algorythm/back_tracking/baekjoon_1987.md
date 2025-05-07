# 1987번: 알파벳

세로 `R`칸, 가로 `C`칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

## 입출력

### 입력
첫째 줄에 `R`과 `C`가 빈칸을 사이에 두고 주어진다. ($1 ≤ R,C ≤ 20$) 둘째 줄부터 $R$개의 줄에 걸쳐서 보드에 적혀 있는 `C`개의 대문자 알파벳들이 빈칸 없이 주어진다

### 출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.

## 예제

### 예제 입력 1

```text
2 4
CAAB
ADCB
```

### 예제 출력 1

```text
3
```

### 예제 입력 2

```text
3 6
HFDFFB
AJHGDH
DGAGEH
```

### 예제 출력 2

```text
6
```

### 예제 입력 3

```text
5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
```

### 예제 출력 3

```text
10
```

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색
- 백트래킹
- 격자 그래프

## 시도

### 시도1

`dfs`를 이용해, 처음 시작할 때의 이동 값을 저장하고, 이동 가능한 모든 경로를 탐색한다.

더이상 탐색할 경로가 없으면 현재까지의 최댓값을 반환한다.

를 바탕으로 코드를 작성했는데, 시간 초과 발생 

```python
import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graphs, direction, r, c, current, repository=[]):
    x, y = direction
    repository.append(graphs[x][y])
    result = current

    for dx, dy in DIRECTIONS:
        row, col = dx + x, dy + y

        if 0 <= row < r and 0 <= col < c and graphs[row][col] not in repository:
            current = max(dfs(graphs, (row, col), r, c, result + 1), current)
            repository.pop()

    return current


R, C = map(int, input().split())
boards = [list(input().rstrip()) for _ in range(R)]
# R, C = 2, 4
# boards = [
#     ["C", "A", "A", "B"],
#     ["A", "D", "C", "B"]
# ]
# R, C = 3, 6
# boards = [
#     list("HFDFFB"),
#     list("AJHGDH"),
#     list("DGAGEH"),
# ]

print(dfs(boards, (0, 0), R, C, 1))
```

### 시도2

알파벳을 직접 저장하는 것이 아닌 아스키코드값으로 접근하였으나, 시간 초과 발생

```python
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graphs, direction, r, c, current, visited):
    x, y = direction
    visited[ord(graphs[x][y]) - 65] = True
    result = current

    for dx, dy in DIRECTIONS:
        row, col = dx + x, dy + y

        if 0 <= row < r and 0 <= col < c and not visited[ord(graphs[row][col]) - 65]:
            current = max(dfs(graphs, (row, col), r, c, result + 1, visited), current)
            visited[ord(graphs[row][col]) - 65] = False

    return current


R, C = map(int, input().split())
boards = [list(input().rstrip()) for _ in range(R)]

v = [False] * 26

print(dfs(boards, (0, 0), R, C, 1, v))
```

### 시도3

문자열을 입력받을 때 부터 아스키코드로 저장하고, visited를 아스키코드값을 이용해서 접근하였으나,
시간 초과 발생

```python
import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graphs, direction, r, c, current, visited):
    global answer
    x, y = direction
    visited[graphs[x][y]] = True
    answer = max(answer, current)

    for dx, dy in DIRECTIONS:
        row, col = dx + x, dy + y

        if 0 <= row < r and 0 <= col < c and not visited[graphs[row][col]]:
            dfs(graphs, (row, col), r, c, current + 1, visited)
            visited[graphs[row][col]] = False


R, C = map(int, input().split())
boards = [list(map(lambda c: ord(c) - 65, input().strip())) for _ in range(R)]
v = [False] * 26
answer = 0
dfs(boards, (0, 0), R, C, 1, v)
print(answer)
```

### 시도4(174488kb, 5000ms)

current를 계속 넘겨주지 않고, answer을 global로 사용하여 최댓값을 저장함 

pypy3를 이용하여 문제 해결

```python
import sys

input = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(graphs, direction, r, c, current, visited):
    global answer
    x, y = direction
    visited[graphs[x][y]] = True
    answer = max(answer, current)

    if answer == 26:
        return

    for dx, dy in DIRECTIONS:
        row, col = dx + x, dy + y

        if 0 <= row < r and 0 <= col < c and not visited[graphs[row][col]]:
            dfs(graphs, (row, col), r, c, current + 1, visited)
            visited[graphs[row][col]] = False


R, C = map(int, input().split())
boards = [list(map(lambda c: ord(c) - 65, input().strip())) for _ in range(R)]
v = [False] * 26
answer = 0
dfs(boards, (0, 0), R, C, 1, v)
print(answer)
```

## 정리

