# [16234번: 인구 이동](https://www.acmicpc.net/problem/16234)

N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는
1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

### 출력

인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.

## 예제

### 예제 입력 1

```text
2 20 50
50 30
20 40
```

### 예제 출력 1

```text
1
```

초기 상태는 아래와 같다.

![img1.png](baekjoon_16234(1).png)

L = 20, R = 50 이기 때문에, 모든 나라 사이의 국경선이 열린다. (열린 국경선은 점선으로 표시)

baekjoon_16234(1)
![img2.png](baekjoon_16234(2).png)

연합은 하나 존재하고, 연합의 인구는 (50 + 30 + 20 + 40) 이다. 연합의 크기가 4이기 때문에, 각 칸의 인구수는 140/4 = 35명이 되어야 한다.

![img3.png](baekjoon_16234(3).png)

### 예제 입력 2

```text
2 40 50
50 30
20 40
```

### 예제 출력 2

```text
0
```

### 예제 입력 3

```text
2 20 50
50 30
30 40
```

### 예제 출력 3

```text
1
```

초기 상태는 아래와 같다.

![img.png](baekjoon_16234(4).png)

L = 20, R = 50이기 때문에, 아래와 같이 국경선이 열린다.

![img_1.png](baekjoon_16234(5).png)

인구 수는 합쳐져있는 연합의 인구수는 (50+30+30) / 3 = 36 (소수점 버림)이 되어야 한다.

![img_2.png](baekjoon_16234(6).png)

### 예제 입력 4

```text
3 5 10
10 15 20
20 30 25
40 22 10
```

### 예제 출력 4

```text
2
```

### 예제 입력 5

```text
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10
```

### 예제 출력 5

```text
3
```

## 알고리즘 분류

- 구현
- 그래프 이론
- 그래프 탐색
- 시뮬레이션
- 너비 우선 탐색

## 시도

### 시도1

헷갈렸던 부분들

1. current의 주위에 있는 나라를 어떻게 탐색할 것인가
   - 알고리즘 분류 힌트를 보고 BFS로 접근했다. 
2. 문제를 제대로 읽지 않아, 처음에는 국경선이 열린 모든 나라의 합을 구해서 평균을 냈었지만,
   반례를 통해 국경이 열린 나라들끼리 평균을 내는 것으로 수정함

국경을 어떻게 추가할지에 대해서도 많이 고민을 해보았던 문제이다.

국경을 추가하는 해결책은, 한 번의 BFS로 탐색한 것들을 모두 하나의 국경으로 취급하였다. 

```python
# https://www.acmicpc.net/problem/16234
# 인구 이동
import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(q, arr, l, r, current, visited):
    result = []
    need_visited = deque([current])

    while need_visited:
        x, y = need_visited.pop()
        visited[x][y] = True
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in result:
                if l <= abs(arr[nx][ny] - arr[x][y]) <= r:
                    result.append((nx, ny))
                    need_visited.append((nx, ny))

    if result:
        q.append(result)
    return


N, L, R = map(int, input().split())  # L 이상, R 이하
populations = [list(map(int, input().split())) for _ in range(N)]
# N, L, R = 2, 20, 50
# populations = [[50, 30], [20, 40]]
# N, L, R = 2, 40, 50
# populations = [[50, 30], [20, 40]]
# N, L, R = 2, 20, 50
# populations = [[50, 30], [30, 40]]
# N, L, R = 3, 5, 10
# populations = [[10, 15, 20], [20, 30, 25], [40, 22, 10]]
# N, L, R = 3, 34, 52
# populations = [[46, 44, 4], [33, 47, 0], [19, 35, 78]]
# N, L, R = 2, 7, 79
# populations = [[21, 8], [86, 77]]

answer = 0
while True:
    queue = []
    v = [[False] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if not v[row][col]:
                bfs(queue, populations, L, R, (row, col), v)

    if not queue:
        break

    for graph in queue:
        total = sum([populations[_x][_y] for _x, _y in graph])
        for r, c in graph:
            populations[r][c] = total // len(graph)

    answer += 1

print(answer)
```

## 정리

