# [1753번: 최단 경로](https://www.acmicpc.net/problem/1753)

방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

## 입출력

### 입력

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

### 출력

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

## 예제

### 예제 입력 1

```text
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
```

### 예제 출력 1

```text
0
2
3
7
INF
```

## 알고리즘 분류

- 그래프 이론
- 최단 경로
- 데이크스트라

## 시도

### 시도1(69300kb, 660ms)

이 문제 역시 다익스트라(데이크스트라) 분류를 통해 들어온 문제라서 바로 다익스트라 문제라는 것을 파악했다.

또한, 시작 노드로부터 모든 정점에 대한 최단 경로를 구하는 문제이기 때문에 다익스트라로 문제를 해결할 수 있다 생각할 수 있을 거라고 생각한다.

`heapq(우선순위 큐)`를 이용하여 문제를 해결하였다. 

```python
# https://www.acmicpc.net/problem/1753
# 최단경로
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

V, E = map(int, input().split())
K = int(input())
graphs = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graphs[u].append((v, w))

distances = [INF for _ in range(V + 1)]
distances[K] = 0

q = []
heapq.heappush(q, (0, K))
while q:
    current_cost, current_node = heapq.heappop(q)

    if distances[current_node] < current_cost:
        continue

    for next_node, next_cost in graphs[current_node]:
        cost = current_cost + next_cost
        if distances[next_node] > cost:
            distances[next_node] = cost
            heapq.heappush(q, (cost, next_node))

for index in range(1, V + 1):
    if distances[index] == INF:
        print("INF")
    else:
        print(distances[index])
```

### 시도2(시간 초과)

`heapq` 라이브러리 없이 직접 다익스트라 코드를 작성하여 문제를 해결해봤다.

시간 초과 발생

```python
# https://www.acmicpc.net/problem/1753
# 최단경로
import sys

input = sys.stdin.readline
INF = int(1e10)

V, E = map(int, input().split())
K = int(input())
graphs = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    graphs[u].append((v, w))

distances = [INF] * (V + 1)
visited = [False] * (V + 1)


def get_smallest_index():
    smallest = INF
    index = 0

    for i in range(1, V + 1):
        if distances[i] < smallest and not visited[i]:
            smallest = distances[i]
            index = i

    return index


def dijkstra(start):
    distances[start] = 0
    visited[start] = True

    for node, weight in graphs[start]:  # start가 방문할 수 있는 모든 노드들에 대해 이동 값 초기화 (후에 인덱스를 결정하기 위함도 있음)
        distances[node] = weight

    for i in range(V - 1):  # 시작 노드는 방문할 필요 없으니까 n - 1
        current = get_smallest_index()  # 가중치가 가장 작은 인덱스를 찾아냄
        visited[current] = True

        for node, weight in graphs[current]:
            cost = weight + distances[current]
            if distances[node] > cost:
                distances[node] = cost


dijkstra(K)

for now in range(1, len(distances)):
    if distances[now] == INF:
        print("INF")
    else:
        print(distances[now])
```

## 정리

