# 2644번: 촌수계산

# 문제

우리 나라는 가족 혹은 친척들 사이의 관계를 촌수라는 단위로 표현하는 독특한 문화를 가지고 있다. 이러한 촌수는 다음과 같은 방식으로 계산된다. 기본적으로 부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의
촌수를 계산한다. 예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로 나와 할아버지는 2촌이 되고, 아버지 형제들과 할아버지는 1촌, 나와 아버지 형제들과는 3촌이 된다.

여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

## 입출력

### 입력

사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다. 입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고, 둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가
주어진다. 그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다. 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다. 이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모
번호를 나타낸다.

각 사람의 부모는 최대 한 명만 주어진다.

### 출력

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다. 어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.

## 예제

### 예제 입력 1

```text
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

### 예제 출력 1

```text
3
```

### 예제 입력 2

```text
9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

### 예제 출력 2

```text
-1
```

## 시도

### 시도1(오답)

`a -> b`에 대해 몇 촌인지 알아내는 문제이다.

1달 전에 풀었던 문제라 정확히 어떻게 접근했는지 기억이 안 나지만, `dfs`를 이용해서 문제를 해결해보려고 했으나, 오답

```python
import sys

input = sys.stdin.readline


def dfs(graph, idx, target):
    if not graph[idx]:
        print(-1)
        exit()

    count = 1
    if target not in graph[idx]:
        return count + dfs(graph, idx + 1, target)

    return count + 1


N = int(input())
relationships = [[] * (N + 1) for _ in range(N + 1)]
person1, person2 = map(int, input().split())
M = int(input())

for _ in range(M):
    parent, child = map(int, input().split())
    relationships[parent].append(child)
    relationships[child].append(parent)

for index in range(N + 1):
    if person1 in relationships[index]:
        print(dfs(relationships, index, person2))
        break
    elif person2 in relationships[index]:
        print(dfs(relationships, index, person1))
        break
```

### 시도2(34944kb, 56ms)

`bfs`로 성공

```python
# https://www.acmicpc.net/problem/2644
# 촌수계산
# TODO: Here !
import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e10)


def dfs(graph, visit, idx, target, count=1):
    print("count:", count)
    visit[idx] = True

    if idx == target:
        return count

    for p in graph[idx]:
        if not visit[p]:
            dfs(graph, visit, p, target, count + 1)


N = int(input())
relationships = [[] for _ in range(N + 1)]
start, end = map(int, input().split())
M = int(input())

for _ in range(M):
    parent, child = map(int, input().split())
    relationships[parent].append(child)
    relationships[child].append(parent)

need_visited = deque([start])
visited = [INF] * (N + 1)
visited[start] = 0

while need_visited:
    current = need_visited.popleft()

    for person in relationships[current]:
        if visited[person] == INF:
            need_visited.append(person)
            visited[person] = visited[current] + 1

if visited[end] == INF:
    print(-1)
else:
    print(visited[end])
```

### 시도3(32412kb, 32ms)

조금 성장한 후에 `dfs`로 도전 후 성공

```python
# https://www.acmicpc.net/problem/2644
# 촌수계산
import sys

input = sys.stdin.readline


def dfs(graph, visited, current, target, count=0):
    if current == target:
        print(count)
        exit()

    for p in graph[current]:
        if not visited[p]:
            visited[p] = True
            dfs(graph, visited, p, target, count + 1)

    return -1


N = int(input())
relationships = [[] * (N + 1) for _ in range(N + 1)]
start, end = map(int, input().split())
M = int(input())

for _ in range(M):
    parent, child = map(int, input().split())
    relationships[parent].append(child)
    relationships[child].append(parent)

print(dfs(relationships, [False] * (N + 1), start, end))
```

## 정리

빠르게 조건을 만족하는 걸 찾으려면 보통 `bfs`로 사용하는 걸로 알고 있는데, 코드의 성능 차이도 있겠지만 이 문제는 `dfs`가 더 빠르다.
