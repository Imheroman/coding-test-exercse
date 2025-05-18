# [16953번: A → B](https://www.acmicpc.net/problem/16953)

정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

2를 곱한다.
1을 수의 가장 오른쪽에 추가한다.
A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

## 입출력

### 입력

첫째 줄에 A, B (1 ≤ A < B ≤ 10<sup>9</sup>)가 주어진다.

### 출력

A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.

## 예제

### 예제 입력 1

```text
2 162
```

### 예제 출력 1

```text
5
```

### 예제 입력 2

```text
4 42
```

### 예제 출력 2

```text
-1
```

### 예제 입력 3

```text
100 40021
```

### 예제 출력 3

```text
5
```

## 알고리즘 분류

- 그래프 이론
- 그리디 알고리즘
- 그래프 탐색
- 너비 우선 탐색
- 집합과 맵

## 시도

### 시도1(메모리 초과)

수에 * 2와 마지막 자리에 + 1을 해서 특정 수와 동일해지게 만드는 문제이다.

`visited`를 이용해서 방문한 숫자에 대해 중복을 제거하고 싶었으나, b가 10<sup>9</sup>이여서 그런지 메모리 초과가 발생했다.

```python
# https://www.acmicpc.net/problem/16953
# A -> B
import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
visited = [False] * (b + 1)
need_visited = deque([(1, a)])
while need_visited:
    weight, node = need_visited.popleft()

    if node == b:
        print(weight)
        exit()

    for n in [int(str(node) + "1"), node * 2]:
        if n <= b and not visited[n]:
            need_visited.append((weight + 1, n))
            visited[n] = True

print(-1)
```

### 시도2(35040kb, 112ms)

visited 제거 후 정답

```python
# https://www.acmicpc.net/problem/16953
# A -> B
import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
# a, b = 2, 162
# a, b = 4, 42
# a, b = 100, 40021
visited = [False] * (b + 1)
need_visited = deque([(1, a)])
while need_visited:
    count, current = need_visited.popleft()

    if current == b:
        print(count)
        exit()

    for n in [int(str(current) + "1"), current * 2]:
        if n <= b and not visited[n]:
            need_visited.append((count + 1, n))
            visited[n] = True

print(-1)
```