# [14503번: 로봇 청소기](https://www.acmicpc.net/problem/14503)

로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램을 작성하시오.

로봇 청소기가 있는 방은 `N x M` 크기의 직사각형으로 나타낼 수 있으며, `1 x 1` 크기의 정사각형 칸으로 나누어져 있다. 각각의 칸은 벽 또는 빈 칸이다.
청소기는 바라보는 방향이 있으며, 이 방향은 동, 서, 남, 북 중 하나이다.
방의 각 칸은 좌표 `(r, c)`로 나타낼 수 있고, 가장 북쪽 줄의 가장 서쪽 칸의 좌표가 `(0, 0)`, 가장 남쪽 줄의 가장 동쪽 칸의 좌표가 `(N-1, M-1)`이다. 즉, 좌표 `(r, c)`는
북쪽에서 `(r+1)`번째에 있는 줄의 서쪽에서 `(c+1)`번째 칸을 가리킨다. 처음에 빈 칸은 전부 청소되지 않은 상태이다.

로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 `4`칸 중 청소되지 않은 빈 칸이 없는 경우,
  1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
  2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 `4`칸 중 청소되지 않은 빈 칸이 있는 경우,
  1. 반시계 방향으로 90&deg; 회전한다.
  2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
  3. 1번으로 돌아간다.

## 입출력

### 입력

첫째 줄에 방의 크기 $N$과 $M$이 입력된다. `(3 <= N, M <= 50)`둘째 줄에 처음에 로봇 청소기가 있는 칸의 좌표 `(r, c)`와 처음에 로봇 청소기가 바라보는 방향 `d`가 입력된다. `d`
가 `0`인 경우 북쪽, `1`인 경우 동쪽, `2`인 경우 남쪽, `3`인 경우 서쪽을 바라보고 있는 것이다.

셋째 줄부터 `N`개의 줄에 각 장소의 상태를 나타내는 `N x M`개의 값이 한 줄에 `M`개씩 입력된다. `i`번째 줄의 `j`번째 값은 칸 `(i, j)`의 상태를 나타내며, 이 값이 `0`인
경우 `(i, j)`가 청소되지 않은 빈 칸이고, `1`인 경우 `(i, j)`에 벽이 있는 것이다. 방의 가장 북쪽, 가장 남쪽, 가장 서쪽, 가장 동쪽 줄 중 하나 이상에 위치한 모든 칸에는 벽이 있다. 로봇
청소기가 있는 칸은 항상 빈 칸이다.

### 출력

로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.

## 예제

### 예제 입력 1

```text
3 3
1 1 0
1 1 1
1 0 1
1 1 1
```

### 예제 출력 1

```text
1
```

### 예제 입력 2

```text
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
```

### 예제 출력 2

```text
57
```

## 알고리즘 분류

- 구현
- 시뮬레이션

## 시도

### 시도1(32412kb, 44ms)

문제를 제대로 읽지 않아 놓친 부분이 많았다.

1. 후진할 때 후진하는 장소가 벽일 시 정지
2. 반시계방향고, 방향이 헷갈려서 인터넷에 검색 후 그림을 보고 대충 풀었었지만 시계방향으로 풀고 있었음
3. 방문했다는 값을 `spaces[row][col] = 1` 로 사용하고 있었는데, 벽인 줄 알고 검색을 멈춤 ,,
4. 오타,,,,,

등등의 사소한 문제가 쌓여 문제를 해결하는데 오랜 시간이 걸렸다.

방향을 설정하는 부분 (`direction = (direction + 3) % 4`)은 [빠르고 꾸준하게](https://resilient-923.tistory.com/164)님의 블로그를 참고하였다.

`direction = (direction + 3) % 4` 와 같이 작성하면, 양의 정수로만 반복되며 -1을 할 수 있게 된다.

[코딩하는 엔지](https://code-angie.tistory.com/29#google_vignette)님의 블로그에서 얻은 아이디어인데, 
파이썬의 장점을 활용하여 `d = (d - 1) % 4` 그냥 음의 인덱스로 접근해도 괜찮었겠다는 생각을 했다.

```python
# https://www.acmicpc.net/problem/14503
# 로봇 청소기
import sys

input = sys.stdin.readline

DIRECTIONS = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}  # 반시계방향

N, M = map(int, input().split())
row, col, direction = list(map(int, input().split()))  # (r, c) d(바라보는 방향)
spaces = [list(map(int, input().split())) for _ in range(N)]
# N, M = 3, 3
# row, col, direction = list(map(int, "1 1 0".split()))  # (r, c) d(바라보는 방향)
# spaces = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# N, M = 11, 10
# row, col, direction = list(map(int, "7 4 0".split()))  # (r, c) d(바라보는 방향)
# spaces = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

answer = 1
spaces[row][col] = 2

while True:
    for _ in range(4):
        direction = (direction + 3) % 4
        x, y = DIRECTIONS[direction]
        if 0 <= row + x < N and 0 <= col + y < M and spaces[row + x][col + y] == 0:
            row, col = row + x, col + y
            spaces[row][col] = 2
            answer += 1
            break
    else:
        x, y = DIRECTIONS[(direction + 2) % 4]  # 후진 방향(총 4개의 방향에 동 <-> 서, 북 <-> 남으로 후진을 하기 때문에, +2를 하고 총 크기인 4로 나눠주면 된다.)
        row, col = row + x, col + y  # 후진
        if not (0 <= row < N and 0 <= col < M) or spaces[row][col] == 1:
            break

print(answer)
```

## 정리

문제를 잘 읽고 이해하자
