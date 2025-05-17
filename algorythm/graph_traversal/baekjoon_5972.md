# [5972번: 택배 배송](https://www.acmicpc.net/problem/5972)

농부 현서는 농부 찬홍이에게 택배를 배달해줘야 합니다. 그리고 지금, 갈 준비를 하고 있습니다. 평화롭게 가려면 가는 길에 만나는 모든 소들에게 맛있는 여물을 줘야 합니다. 물론 현서는 구두쇠라서 최소한의 소들을
만나면서 지나가고 싶습니다.

농부 현서에게는 지도가 있습니다. N (1 <= N <= 50,000) 개의 헛간과, 소들의 길인 M (1 <= M <= 50,000) 개의 양방향 길이 그려져 있고, 각각의 길은 C_i (0 <= C_i <=
1,000) 마리의 소가 있습니다. 소들의 길은 두 개의 떨어진 헛간인 A_i 와 B_i (1 <= A_i <= N; 1 <= B_i <= N; A_i != B_i)를 잇습니다. 두 개의 헛간은 하나 이상의 길로
연결되어 있을 수도 있습니다. 농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.

다음 지도를 참고하세요.

```text
           [2]---
          / |    \
         /1 |     \ 6
        /   |      \
     [1]   0|    --[3]
        \   |   /     \2
        4\  |  /4      [6]
          \ | /       /1
           [4]-----[5] 
                3  
```

농부 현서가 선택할 수 있는 최선의 통로는 1 -> 2 -> 4 -> 5 -> 6 입니다. 왜냐하면 여물의 총합이 1 + 0 + 3 + 1 = 5 이기 때문입니다.

농부 현서의 지도가 주어지고, 지나가는 길에 소를 만나면 줘야할 여물의 비용이 주어질 때 최소 여물은 얼마일까요? 농부 현서는 가는 길의 길이는 고려하지 않습니다.

## 입출력

### 입력

첫째 줄에 N과 M이 공백을 사이에 두고 주어집니다.

둘째 줄부터 M+1번째 줄까지 세 개의 정수 A_i, B_i, C_i가 주어집니다.

### 출력

첫째 줄에 농부 현서가 가져가야 될 최소 여물을 출력합니다.

## 예제

### 예제 입력 1

```text
6 8
4 5 3
2 4 0
4 1 4
2 1 1
5 6 1
3 6 2
3 2 6
3 4 4
```

### 예제 출력 1

```text
5
```

## 알고리즘 분류

- 그래프 이론
- 최단 경로
- 데이크스트라

## 시도

### 시도1(52284kb, 208ms)

시작 노드(1)로부터 최솟값으로 목적지(N)까지 도달하는 것이다.

그래프를 이용해서 시작 위치부터 최솟값으로 목적지에 도달하는 값을 구하는 것이기 때문에,
다익스트라 알고리즘을 이용해서 문제를 해결했다.

```python
# https://www.acmicpc.net/problem/5972
# 택배 배송
import heapq
import sys

input = sys.stdin.readline
# DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
INF = int(1e10)

N, M = map(int, input().split())
graphs = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, weight = map(int, input().split())
    graphs[_from].append((_to, weight))
    graphs[_to].append((_from, weight))


def dijkstra(graph, start):
    distances = [INF] * (N + 1)
    distances[0] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        current_weight, now = heapq.heappop(q)

        if distances[now] < current_weight:
            continue

        for next_node, next_weight in graph[now]:
            cost = current_weight + next_weight

            if distances[next_node] > cost:
                distances[next_node] = cost
                heapq.heappush(q, (cost, next_node))

    print(distances)
    print(distances[N])


dijkstra(graphs, 1)
```

## 정리

