# [1238번: 파티](https://www.acmicpc.net/problem/1238)

N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다.

어느 날 이 N명의 학생이 X (1 ≤ X ≤ N)번 마을에 모여서 파티를 벌이기로 했다. 이 마을 사이에는 총 M개의 단방향 도로들이 있고 i번째 길을 지나는데 Ti(1 ≤ Ti ≤ 100)의 시간을 소비한다.

각각의 학생들은 파티에 참석하기 위해 걸어가서 다시 그들의 마을로 돌아와야 한다. 하지만 이 학생들은 워낙 게을러서 최단 시간에 오고 가기를 원한다.

이 도로들은 단방향이기 때문에 아마 그들이 오고 가는 길이 다를지도 모른다. N명의 학생들 중 오고 가는데 가장 많은 시간을 소비하는 학생은 누구일지 구하여라.

## 입출력

### 입력

첫째 줄에 N(1 ≤ N ≤ 1,000), M(1 ≤ M ≤ 10,000), X가 공백으로 구분되어 입력된다. 두 번째 줄부터 M+1번째 줄까지 i번째 도로의 시작점, 끝점, 그리고 이 도로를 지나는데 필요한
소요시간 Ti가 들어온다. 시작점과 끝점이 같은 도로는 없으며, 시작점과 한 도시 A에서 다른 도시 B로 가는 도로의 개수는 최대 1개이다.

모든 학생들은 집에서 X에 갈수 있고, X에서 집으로 돌아올 수 있는 데이터만 입력으로 주어진다.

### 출력

첫 번째 줄에 N명의 학생들 중 오고 가는데 가장 오래 걸리는 학생의 소요시간을 출력한다.

## 예제

### 예제 입력 1

```text
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
```

### 예제 출력 1

```text
10
```

## 알고리즘 분류

- 그래프 이론
- 최단 경로
- 데이크스트라

## 시도

### 시도1(73016kb, 1692ms)

처음에는, 문제 이해를 잘못해서(꼼꼼하게 안 읽음) X까지 도달하는 최장 거리를 구하는 줄 알았다.

하지만, 왕복하는 문제였고, 이 또한 단순히 최단 거리를 구해진 것에서 *2를 하면 왕복이 될 거라고 생각했다.

이는 당연하게 예제 입력1에 대한 예제 출력1의 결과와 다른 답이 나왔고, 곰곰히 생각해보니

각 학생들이 X까지 최단 거리로 도달하고, X에서 각 학생들에게 최단 거리로 갔을 떄,
최장 거리를 구하면 된다고 생각이 들어 다익스트라(데이크스트라)로 구현을 했고, 정답을 맞췄다.

```python
# https://www.acmicpc.net/problem/1238
# 파티
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)

N, M, X = map(int, input().split())
graphs = [[] for _ in range(N + 1)]

for _ in range(M):
    _from, _to, time = map(int, input().split())
    graphs[_from].append((_to, time))

distances = [[INF] * (N + 1) for _ in range(N + 1)]

for student in range(1, N + 1):
    distances[student][student] = 0
    q = []
    heapq.heappush(q, (0, student))

    while q:
        current_weight, now = heapq.heappop(q)

        if distances[student][now] < current_weight:
            continue

        for next_node, next_weight in graphs[now]:
            cost = next_weight + current_weight
            if distances[student][next_node] > cost:
                distances[student][next_node] = cost
                heapq.heappush(q, (cost, next_node))

answer = -1
for student in range(1, N + 1):
    if student == X:
        continue

    result = distances[student][X] + distances[X][student]

    answer = max(answer, result)

print(answer)
```