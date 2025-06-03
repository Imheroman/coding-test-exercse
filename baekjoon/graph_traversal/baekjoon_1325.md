# [1325번: 효율적인 해킹](https://www.acmicpc.net/problem/1325)

해커 김지민은 잘 알려진 어느 회사를 해킹하려고 한다. 이 회사는 N개의 컴퓨터로 이루어져 있다. 김지민은 귀찮기 때문에, 한 번의 해킹으로 여러 개의 컴퓨터를 해킹 할 수 있는 컴퓨터를 해킹하려고 한다.

이 회사의 컴퓨터는 신뢰하는 관계와, 신뢰하지 않는 관계로 이루어져 있는데, A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.

이 회사의 컴퓨터의 신뢰하는 관계가 주어졌을 때, 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 출력하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에, N과 M이 들어온다. 
N은 10,000보다 작거나 같은 자연수, M은 100,000보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에 신뢰하는 관계가 A B와 같은 형식으로 들어오며, "A가 B를 신뢰한다"를 의미한다. 컴퓨터는 1번부터 N번까지 번호가 하나씩 매겨져 있다.

### 출력
첫째 줄에, 김지민이 한 번에 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

## 예제

### 예제 입력 1

```text
5 4
3 1
3 2
4 3
5 3
```

### 예제 출력 1

```text
1 2
```

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 시도

### 시도1(시간 초과 - Python3 / 169612kb, 10976ms - PyPy3)

연결되어 있는 그래프끼리 가장 많이 연결되어 있는 노드를 출력하는 문제이다.

`A가 B를 신뢰하는 경우에는 B를 해킹하면, A도 해킹할 수 있다는 소리다.`를 보고,
B가 해킹 당했을 때, A를 해킹할 수 있다 == B에서 A를 방문할 수 있다 로 생각했다.

1. B가 A를 잇는 그래프를 그린다.
2. 현재 그래프와 연결된 그래프를 탐색한다(bfs, dfs, ...).
3. 가장 많이 연결된 그래프 리스트를 찾는다.

```python
# https://www.acmicpc.net/problem/1325
# 효율적인 해킹
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
relationships = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    relationships[b].append(a)

_max = 0
answer = []


def bfs(arr, n, start):
    visited = [False] * (n + 1)
    visited[start] = True
    need_visited = deque([start])
    count = 1
    while need_visited:
        now = need_visited.popleft()

        for node in arr[now]:
            if not visited[node]:
                visited[node] = True
                need_visited.append(node)
                count += 1

    return count


for current in range(1, N + 1):
    if len(relationships[current]) == 0:
        continue

    result = bfs(relationships, N, current)

    if result == _max:
        answer.append(current)
    elif result > _max:
        _max = result
        answer.clear()
        answer.append(current)

print(*answer)
```