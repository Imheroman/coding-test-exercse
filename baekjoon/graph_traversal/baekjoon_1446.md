# [1446번: 지름길](https://www.acmicpc.net/problem/1446)

매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게
되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

## 입출력

### 입력

첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가
주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

### 출력

세준이가 운전해야하는 거리의 최솟값을 출력하시오.

## 예제

### 예제 입력 1

```text
5 150
0 50 10
0 50 20
50 100 10
100 151 10
110 140 90
```

### 예제 출력 1

```text
70
```

### 예제 입력 2

```text
2 100
10 60 40
50 90 20
```

### 예제 출력 2

```text
80
```

### 예제 입력 3

```text
8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0
```

### 예제 출력 3

```text
432
```

## 알고리즘 분류

## 시도

### 시도1(35508kb, 40ms)

그냥 [개발 어린이의 성장 일기](https://velog.io/@cku7808/백준Python-1446-지름길)님의 코드이다.

코드를 이해하고 내 방식대로 작성해보려고 했으나, 다익스트라 문제를 1-2문제밖에 안 풀어봐서 그런지 아직 접근이 어려웠다.

```python
graphs = [[] for num in range(D + 1)]
# ...
for i in range(D):
    graphs[i].append((i+1, 1))  # 현재 그래프에서 갈 수 있는 곳을 저장한다. D 까지만 하는 이유는 D는 목적지이기 때문에, 다음 방향이 없어야 하기 때문이다.
```

을 이용하여, 고속도로의 거리 값을 초기화할 수 있다는 것을 배웠다.



내가 이해하고 작성한 부분은 주석으로 달았다.

```python
# https://www.acmicpc.net/problem/1446
# 지름길
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, D = map(int, input().split())
graphs = [[] for num in range(D + 1)]

for i in range(D):
    graphs[i].append((i+1, 1))  # 현재 그래프에서 갈 수 있는 곳을 저장한다. D 까지만 하는 이유는 D는 목적지이기 때문에, 다음 방향이 없어야 하기 때문이다.

for _ in range(N):
    start, destination, weight = map(int, input().split())
    if destination <= D:  # 목적지가 고속도로의 길이보다 짧은 것만 그래프에 추가한다.
        graphs[start].append((destination, weight))

distance = [INF] * (D + 1)  # 출발지로부터의 거리를 측정한다.
distance[0] = 0  # 출발지는 거리를 0으로 설정한다.
q = []  # 이동할 목적지들을 저장하는 곳
heapq.heappush(q, (0, 0))  # 처음 시작지를 추가
while q:  # 방문해야 할 그래프들이 있다면
    w, now = heapq.heappop(q)  # 가중치와, 현재 방문한 인덱스를 뽑아옴

    if distance[now] < w:  # 지금 인덱스보다 가중치가 더 크면, 방문할 필요가 없음
        continue

    for node, c in graphs[now]:  # 방문할 그래프들 중
        cost = c + distance[now]  # 값을 계산하고(경유해서 가는 값)
        if distance[node] > cost:  # 지금 목적지의 값이 경유해서 가는 값보다 크다면 ? 값과 인덱스를 업데이트
            distance[node] = cost
            heapq.heappush(q, (cost, node))

print(distance[D])
```

## 정리

