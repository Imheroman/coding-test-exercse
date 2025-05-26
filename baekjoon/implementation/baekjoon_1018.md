# [1018번: 체스판 다시 칠하기](https://www.acmicpc.net/problem/1018)

지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의
체스판으로 만들려고 한다.

체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면
체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.

보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는
정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

### 출력

첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

## 예제

### 예제 입력 1

```text
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
```

### 예제 출력 1

```text
1
```

### 예제 입력 2

```text
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
```

### 예제 출력 2

```text
12
```

### 예제 입력 3

```text
8 8
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
```

### 예제 출력 3

```text
0
```

### 예제 입력 4

```text
9 23
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBB
BBBBBBBBBBBBBBBBBBBBBBW
```

### 예제 출력 4

```text
31
```

### 예제 입력 5

```text
10 10
BBBBBBBBBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBWBWBWBWB
BWBWBWBWBB
BBBBBBBBBB
```

### 예제 출력 5

```text
0
```

### 예제 입력 6

```text
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWWWB
BWBWBWBW
```

### 예제 출력 6

```text
2
```

### 예제 입력 7

```text
11 12
BWWBWWBWWBWW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
BWWBWBWWWBWW
WBWWBWBBWWBW
BWWBWBBWWBWW
WBWWBWBBWWBW
```

### 예제 출력 7

```text
15
```

## 알고리즘 분류

- 구현
- 브루트포스 알고리즘

## 시도

### 시도1(36084kb, 2664ms)

나는 문제를 너무 어렵게 생각하는 것 같다.

처음 봤을 때, 어떻게 접근해야 할 지 고민이 됐다.

결국, 각 인덱스에서 8개씩 잘라서 W와 B로 시작하는 걸 구분한 후 BFS를 이용해서 전체 인덱스를 탐색했다.

```python
# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기
import copy
import sys
from collections import deque

input = sys.stdin.readline
BOARD_SIZE = 8
DIRECTIONS = [(0, 1), (1, 0)]

N, M = map(int, input().split())
graphs = [list(input().rstrip()) for _ in range(N)]

answer = int(1e10)
for i in range(N - BOARD_SIZE + 1):  # 8개를 뺀 만큼 (보드 크기가 8임)
    for j in range(M - BOARD_SIZE + 1):  # 8개를 뺀 만큼 (보드 크기가 8임)
        for k in range(2):  # W로 시작할 때와 B로 시작할 때를 구분
            copy_graphs = copy.deepcopy(graphs)
            need_visited = deque()
            need_visited.append((i, j))
            visited = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]
            visited[0][0] = True
            result = 0

            if k == 0:  # B로 시작할 때
                if copy_graphs[i][j] != "B":
                    result += 1
                    copy_graphs[i][j] = "B"
            else:  # W로 시작할 때
                if copy_graphs[i][j] != "W":
                    result += 1
                    copy_graphs[i][j] = "W"

            while need_visited:  # BFS
                x, y = need_visited.popleft()

                for dx, dy in DIRECTIONS:
                    row, col = x + dx, y + dy

                    if i <= row < i + BOARD_SIZE and j <= col < j + BOARD_SIZE and not visited[row - i][col - j]:
                        visited[row - i][col - j] = True
                        need_visited.append((row, col))

                        if copy_graphs[row][col] == copy_graphs[x][y]:  # 이전 문자와 같은 문자일 때
                            result += 1
                            if copy_graphs[row][col] == "B":  # 문자 변경
                                copy_graphs[row][col] = "W"
                            else:
                                copy_graphs[row][col] = "B"
            answer = min(answer, result)

print(answer)
```

### 시도2(32412kb, 60ms)

[숨](https://velog.io/@klaus/파이썬Python-백준-1018번-체스판-다시-칠하기)님의 블로그를 보고 작성한 코드

일단 화이트로 시작하는 보드를 정의해놓고, 현재 선택된 보드와 비교한다.

`기존의 결과`와 `화이트 보드` 그리고 `64 - 화이트 보드의 결과 = 검정으로 시작하는 보드의 결과`를 비교한다.

```python
# https://www.acmicpc.net/problem/1018
# 체스판 다시 칠하기
import sys

input = sys.stdin.readline
BOARD_SIZE = 8

DEFAULT_WHITE_BOARD = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW'
]

N, M = map(int, input().split())
graphs = [list(input().rstrip()) for _ in range(N)]

answer = 32  # 변화시킬 수 있는 최대 횟수
for i in range(N - BOARD_SIZE + 1):  # 8개를 뺀 만큼 (보드 크기가 8임)
    for j in range(M - BOARD_SIZE + 1):  # 8개를 뺀 만큼 (보드 크기가 8임)
        result = 0
        for row in range(i, i + BOARD_SIZE):
            for col in range(j, j + BOARD_SIZE):
                # print("row:", row, "col:", col)
                if graphs[row][col] != DEFAULT_WHITE_BOARD[row - i][col - j]:
                    result += 1

        # 기존의 답, W가 첫 인덱스로 시작한 답, 64(8 * 8 == 체스 최대 말 수) 중 W가 첫 인덱스로 시작된 값을 뺀 결과 == 검정이 먼저 시작한 값
        answer = min(answer, result, 64 - result)

print(answer)
```

## 정리

아직 많이 부족한 것 같다.