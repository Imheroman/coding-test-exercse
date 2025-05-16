# [13549번: 숨바꼭질 3](https://www.acmicpc.net/problem/13549)

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의
위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

### 출력

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

## 예제

### 예제 입력 1

```text
5 17
```

### 예제 출력 1

```text
2
```

## 힌트

수빈이가 5-10-9-18-17 순으로 가면 2초만에 동생을 찾을 수 있다.

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 최단 경로
- 데이크스트라
- 0-1 너비 우선 탐색

## 시도

### 시도1(120580kb, 760ms)

다익스트라(데이크스트라)를 풀어와서 그런지 바로 다익스트라로 풀 수 있을 것 같다는 생각이 들었다.

다익스트라보다 DP로 먼저 풀 수 있을 것 같다라고 생각했지만, 아직 점화식을 세우는 데 익숙하지 않아서 다익스트라로 먼저 해결을 해보았다.

`if 0 <= next_node <= MAX - 1 and distances[next_node] > cost:` 부분에서
최대 범위를 `MAX - 1`이 아닌 `K`까지로 설정했었으나, [반례 사이트](https://testcase.ac/problems/13549)에서 계속 오답이 발생했다.

재미나이에게 물어보니 *2 후 갈 수 있는 부분도 범위가 초과되어 못 가서 그럴 것 같다고 하여

시간도 넉넉하기 때문에 일단 MAX로 설정해놓고 문제를 해결했다.

```python
import sys
import heapq

input = sys.stdin.readline
INF = int(1e10)
MAX = 200_000

N, K = map(int, input().split())

if N >= K:
    print(N - K)
    exit()

graphs = [[] for _ in range(MAX)]
distances = [INF] * MAX

for i in range(MAX):
    graphs[i].append((i + 1, 1))
    graphs[i].append((i * 2, 0))

    if i > 0:
        graphs[i].append((i - 1, 1))

distances[N] = 0
q = []
heapq.heappush(q, (0, N))

while q:
    current_weight, now = heapq.heappop(q)

    if current_weight > distances[now]:
        continue

    for next_node, next_weight in graphs[now]:
        cost = current_weight + next_weight

        if 0 <= next_node <= MAX - 1 and distances[next_node] > cost:
            distances[next_node] = cost
            heapq.heappush(q, (cost, next_node))

print(distances[K])
```

## 정리

