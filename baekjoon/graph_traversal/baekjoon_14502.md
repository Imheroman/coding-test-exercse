# [14502번: 연구소](https://www.acmicpc.net/problem/14502)

인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다. 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다. 연구소는 빈 칸, 벽으로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다.

일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼져나갈 수 있다. 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.

예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자.

```text
2 0 0 0 1 1 0  
0 0 1 0 1 2 0  
0 1 1 0 1 0 0  
0 1 0 0 0 0 0  
0 0 0 0 0 1 1  
0 1 0 0 0 0 0  
0 1 0 0 0 0 0  
```

이때, 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다. 아무런 벽을 세우지 않는다면, 바이러스는 모든 빈 칸으로 퍼져나갈 수 있다.

2행 1열, 1행 2열, 4행 6열에 벽을 세운다면 지도의 모양은 아래와 같아지게 된다.

```text
2 1 0 0 1 1 0  
1 0 1 0 1 2 0  
0 1 1 0 1 0 0  
0 1 0 0 0 1 0  
0 0 0 0 0 1 1  
0 1 0 0 0 0 0  
0 1 0 0 0 0 0
```  

바이러스가 퍼진 뒤의 모습은 아래와 같아진다.

```text
2 1 0 0 1 1 2  
1 0 1 0 1 2 2  
0 1 1 0 1 2 2  
0 1 0 0 0 1 2  
0 0 0 0 0 1 1    
0 1 0 0 0 0 0  
0 1 0 0 0 0 0
```

벽을 3개 세운 뒤, 바이러스가 퍼질 수 없는 곳을 안전 영역이라고 한다. 위의 지도에서 안전 영역의 크기는 27이다.

연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 ≤ N, M ≤ 8)

둘째 줄부터 N개의 줄에 지도의 모양이 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치이다. 2의 개수는 2보다 크거나 같고, 10보다 작거나 같은 자연수이다.

빈 칸의 개수는 3개 이상이다.

### 출력

첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.

## 예제

### 예제 입력 1

```text
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
```

### 예제 출력 1

```text
27
```

### 예제 입력 2
```text
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2
```
### 예제 출력 2

```text
9
```
### 예제 입력 3
```text
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
```
### 예제 출력 3

```text
3
```
## 시도

### 시도1

아래와 같이 약 2시간 동안 접근하였으나, 코드가 너무 복잡해졌고 혼자서 구현하기에는 너무 많은 시간을 사용할 것으로 예상되어
다른 블로그를 참고하였음

문제를 풀며 공부한 점

1. `Python`의 `List`는 *Mutable*하다. 
   - 이중 `List`를 copy하면 얕은 복사가 일어나 
     내부 값이 변경된다.
2. 다른 블로그를 조금 공부한 후 느낀 점은 나는 `백트래킹`을 모른다.
   - `백트래킹`을 먼저 공부하고 접근하는 것이 좋을 것 같다.  

정답은 안 나오고, 문제를 풀어보기만 한 코드
```python
# https://www.acmicpc.net/problem/14502
# title
from collections import deque
from sys import stdin
import copy

input = stdin.readline

M, N = 7, 7
graphs = [
    list(map(int, "2 0 0 0 1 1 0".split())),
    list(map(int, "0 0 1 0 1 2 0".split())),
    list(map(int, "0 1 1 0 1 0 0".split())),
    list(map(int, "0 1 0 0 0 0 0".split())),
    list(map(int, "0 0 0 0 0 1 1".split())),
    list(map(int, "0 1 0 0 0 0 0".split())),
    list(map(int, "0 1 0 0 0 0 0".split()))
]
# M, N = map(int, input().rstrip().split())
# graphs = [list(map(int, input().rstrip().split())) for _ in range(M)]
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def virus(g, index):
    need_visited = deque([index])

    while need_visited:
        x, y = need_visited.popleft()

        for dx, dy in DIRECTIONS:
            row, col = x + dx, y + dy
            if 0 <= row < M and 0 <= col < N and g[row][col] == 0:
                need_visited.append((row, col))
                g[row][col] = 2


answer = 0

index_range = N * M
# for i in range(index_range):
for i in range(index_range // 2):
    copy_graph = copy.deepcopy(graphs)
    count = 0
    print("=" * 30, "i:", i, "=" * 30)
    if copy_graph[i // N][i % N] == 0:
        copy_graph[i // N][i % N] = 1
        count += 1
        print("i count")
    for j in range(i + 1, index_range, 1):
        if count == 1 and copy_graph[j // N][j % N] == 0:
            copy_graph[j // N][j % N] = 1
            count += 1
            print("j count")
        for k in range(j + 1, index_range, 1):
            if count == 2 and copy_graph[k // N][k % N] == 0:
                copy_graph[k // N][k % N] = 1
                count += 1
                print("k count")

            if count == 3:
                copy = copy_graph.copy()
                print("before bfs graph")
                for r in range(M):
                    for c in range(N):
                        if copy[r][c] == 2:
                            virus(copy, (r, c))
                print(copy_graph)
                print("after bfs graph")

                result = 0
                for c in copy:
                    print(c)
                    result += c.count(0)
                print(copy_graph)

                if result > answer:
                    print("if i:", i)
                    answer = result
                count = 2

print(answer)

```

### 시도2(35116kb, 7596ms)

백트래킹을 공부하고 순열, 조합 등으로 재귀를 함께 공부한 후 문제를 해결하였다.

처음 벽을 세우는 로직을 순열을 구하는 알고리즘으로 접근하여 순열을 이용해 벽을 세워야 하는 좌표를 구하였다.
(조합으로 해결할 수 있고, 경우의 수가 더 적어 더 빠를 것 같지만, 알고리즘을 순열로 접근했어서 빠른 문제 풀이를 위해 그냥 순열만 진행함)

이후 벽이 3개(문제에서 정해진 벽을 세우는 횟수)가 세워지면 기존 배열을 복사하여 새로운 배열을 만들었고(재사용하기 위해),
해당 배열을 이용하여 BFS를 진행해서 바이러스를 전파하였다.

```python
# https://www.acmicpc.net/problem/14502
# 연구소
from collections import deque
from sys import stdin

input = stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().rstrip().split())
graphs = [list(map(int, input().rstrip().split())) for _ in range(M)]
# M, N = 7, 7
# graphs = [
#     list(map(int, "2 0 0 0 1 1 0".split())),
#     list(map(int, "0 0 1 0 1 2 0".split())),
#     list(map(int, "0 1 1 0 1 0 0".split())),
#     list(map(int, "0 1 0 0 0 0 0".split())),
#     list(map(int, "0 0 0 0 0 1 1".split())),
#     list(map(int, "0 1 0 0 0 0 0".split())),
#     list(map(int, "0 1 0 0 0 0 0".split()))
# ]


def permutations(arr, size):
    answer = 0

    if size == 0:
        copy_graphs = [c[:] for c in arr]

        queue = deque()
        for i in range(M):
            for j in range(N):
                if copy_graphs[i][j] == 2:
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                row, col = x + dx, y + dy
                if 0 <= row < M and 0 <= col < N and copy_graphs[row][col] == 0:
                    queue.append((row, col))
                    copy_graphs[row][col] = 2

        return sum(graph.count(0) for graph in copy_graphs)

    for r in range(M):
        for c in range(N):
            if arr[r][c] == 0:
                arr[r][c] = 1
                answer = max(answer, permutations(arr, size - 1))
                arr[r][c] = 0

    return answer


print(permutations(graphs, 3))
```
