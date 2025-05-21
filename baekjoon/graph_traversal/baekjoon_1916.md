# [1916번: 최소비용 구하기](https://www.acmicpc.net/problem/1916)

N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지
가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

## 입출력

### 입력

첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저
처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.

### 출력

첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

## 예제

### 예제 입력 1

```text
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
```

### 예제 출력 1

```text
4
```

## 알고리즘 분류

- 그래프 이론
- 최단 경로
- 데이크스트라(다익스트라)

## 시도

### 시도1(58232kb, 296ms)

그래프(도시)A에서 그래프(도시)B로 이동하는 최소 거리를 구하는 문제이다.

문제의 유형만 잘 파악하면, 바로 해결할 수 있는 문제인 것 같다.

나는 다익스트라(데이크스트라)의 유형 연습하려고 분류를 지어 문제를 해결하고 있어서 쉽게 해결했다.

```python
# https://www.acmicpc.net/problem/1916
# 최소비용 구하기
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N = int(input())
M = int(input())

graphs = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, weight = map(int, input().split())
    graphs[_from].append((_to, weight))

A, B = map(int, input().split())

distances = [INF for _ in range(N + 1)]
distances[A] = 0
q = []
heapq.heappush(q, (0, A))

while q:
    now_cost, current = heapq.heappop(q)

    if distances[current] < now_cost:  # 현재 방문한 노드의 비용이 기존에 방문했던 노드들의 비용보다 값이 크면 continue
        continue

    for next_node, next_cost in graphs[current]:  # 현재 노드에서 방문할 수 있는 노드들에 대해 반복
        cost = next_cost + now_cost  # 현재 노드의 값과 이동할 노드의 값 계산

        if distances[next_node] > cost:  # 기존의 노드를 방문할 수 있는 값보다 이동해서 가는 값이 더 작으면
            distances[next_node] = cost  # 값 업데이트
            heapq.heappush(q, (cost, next_node))  # 다음 노드로 다시 방문

print(distances[B])
```

## 정리

