# 11725번: 트리의 부모 찾기

루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

## 입출력

### 입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.


### 출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.


## 예제

### 예제 입력 1
```text
7
1 6
6 3
3 5
4 1
2 4
4 7
```
### 예제 출력 1
```text
4
6
1
3
1
4
```

### 예제 입력 2
```text
12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
```

### 예제 출력 2
```text
1
1
2
3
3
4
4
5
5
6
6
```

## 시도

### 시도1 (오답)

그래프에 노드들을 연결해놓고, 처음 연결된 노드들을 출력

```python
# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
import sys

input = sys.stdin.readline

N = int(input())
nodes = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for index in range(2, N + 1):
    print(nodes[index][0])
```

### 시도2

BFS를 이용하여 방문하지 않은 노드들의 부모를 초기화

```python
# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graphs = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graphs[a].append(b)
    graphs[b].append(a)

answer = [-1] * (N + 1)
queue = deque([1])
while queue:
    current = queue.popleft()
    for value in graphs[current]:
        if answer[value] == -1:
            answer[value] = current
            queue.append(value)

for val in answer[2:]:
    print(val)
```

## 정리

아직 어떤 것을 문제가 정확히 이해되지는 않으나, 그냥 그래프 탐색 문제였던 듯 함.

그래프 탐색을 이용하여 방문하지 않은 노드를 초기화 시켜주는 문제였음 
