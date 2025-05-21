# [11724번: 연결 요소의 개수]((https://www.acmicpc.net/problem/11724))

방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠
v) 같은 간선은 한 번만 주어진다.

### 출력

첫째 줄에 연결 요소의 개수를 출력한다.

## 예제 1

### 예제 입력 1

```text
6 5
1 2
2 5
5 1
3 4
4 6
```

### 예제 출력 1

```text
2
```

### 예제 2

### 예제 입력 2

```text
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
```

### 예제 출력 2

```text
1
```

## 시도

### 시도1

이 문제는 최상위 노드가 서로 다른 그래프가 몇 개 인지를 구하는 문제이다. (문제가 이해가 안 돼서 [블로그](https://velog.io/@ssh00n/연결-요소의-개수-zr0w6523) 그림을 보고 참고함)
처음에는 최상위 노드를 구하는 알고리즘(union find)을 이용하여 문제를 해결할 생각이었으나, 다른 사람들이 BFS, DFS를 많이 사용하여 일단 BFS와 DFS를 이용하여 문제를 해결함

BFS

```python
# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수
from collections import deque
from sys import stdin

input = stdin.readline

N, E = map(int, input().split())
graphs = [deque() for i in range(N + 1)]

for _ in range(E):
    n, e = map(int, input().split())
    graphs[n].append(e)
    graphs[e].append(n)

visited = [False] * (N + 1)
need_visited = deque()
answer = 0

for i in range(1, N + 1):  # 1 ~ N
    if not visited[i]:
        answer += 1
        need_visited.append(i)
        while need_visited:
            current = need_visited.popleft()
            if not visited[current]:
                visited[current] = True
                while graphs[current]:
                    need_visited.append(graphs[current].popleft())

print(answer)
```

### 시도 2

DFS

```python
from collections import deque
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(nodes, current, is_visited):
    for value in nodes[current]:
        if not is_visited[value]:
            is_visited[value] = True
            dfs(nodes, value, is_visited)


N, E = map(int, input().split())
graphs = [deque() for i in range(N + 1)]

for _ in range(E):
    n, e = map(int, input().split())
    graphs[n].append(e)
    graphs[e].append(n)

visited = [False] * (N + 1)
answer = 0

for i in range(1, N + 1):  # 1 ~ N
    if not visited[i]:
        answer += 1
        visited[i] = True
        dfs(graphs, i, visited)

print(answer)
```

### 시도 3

union find algorithm 을 이용하여 최상위 노드 탐색 후 병합하여 최상위 노드 수 파악

[union find algorithm 참고 블로그](https://velog.io/@woo0_hooo/알고리즘-union-find-알고리즘)

```python
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def find(nodes, current):
    if nodes[current] != current:  # 최상위 노드가 아닌 경우에 (최상위 노드만 본인의 값이 저장되어 있기 때문에 현재 인덱스와 값이 동일하지 않으면 최상위 노드가 아니다.)
        return find(nodes, nodes[current])  # 최상위 노드 탐색

    return current


def union(nodes, a, b):
    a = find(nodes, a)  # a의 최상위 노드를 찾음
    b = find(nodes, b)  # b의 최상위 노드를 찾음

    if a < b:  # 더 작은 값을 찾아서 더 큰 index에 더 작은 값 대입
        nodes[b] = a
    else:
        nodes[a] = b


N, E = map(int, input().split())
graphs = [i for i in range(N + 1)]

for _ in range(E):
    u, v = map(int, input().split())
    union(graphs, u, v)

answer = set()  # set 자료구조를 이용한 중복 제거

for index in range(1, N + 1):
    answer.add(find(graphs, index))

print(len(answer))
```

## 결과

최적화는 하지 않았지만, 내 코드로만 확인해봤을 때 

BFS: 912ms  
DFS: 652ms  
Union Find Algorithm: 644ms 

의 결과로 Union Find 가 가장 빨랐다.