# [1697번: 숨바꼭질](https://www.acmicpc.net/problem/1697)

수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의
위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠s른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

### 출력

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

## 예제

### 예제 입력 1

5 17

### 예제 출력 1

4

## 시도

### 시도1

DP 방식으로 풀어보려고 했으나, 아직 DP의 알고리즘이 제대로 이해되지 않았음 ,,
코드 작성 조차 실패

결국 다른 분이 작성한 코드를 토대로 이해 후 작성

**나의 코드가 아님 [출처 블로그](https://velog.io/@rltjr1092/백준-1697-숨바꼭질-파이썬)**
```python
# https://www.acmicpc.net/problem/1697
# 숨바꼭질
# 참고 블로그: https://velog.io/@rltjr1092/백준-1697-숨바꼭질-파이썬

from sys import stdin

MAX_SIZE = 100_002

input = stdin.readline

N, K = map(int, input().split())
repository = [float("INF")] * MAX_SIZE

if N >= K:
    print(N - K)
    exit()

for index in range(K + 1):
    repository[index] = abs(index - N)

for index in range(N + 1, K + 1):
    if index % 2 == 0:  # 짝수인 경우
        # index가 2로 나누어지기 때문에 바로 //2를 사용
        repository[index] = min(repository[index - 1] + 1, repository[index // 2] + 1)
    else:  # 홀수인 경우
        # index가 2로 나누어지지 않기 때문에 다음 숫자로 이동 후 이동
        # 따라서 2개를 더함
        repository[index] = min(repository[index - 1] + 1, repository[(index + 1) // 2] + 2)

print(repository[K])
```

### 시도2

BFS로 풀어보려고 했으나, 너무 DP에 사로잡혀 코드를 제대로 작성할 수가 없었고,
다른 사람의 블로그를 참고하여 작성하기로 함

[블로그 주소](https://data-flower.tistory.com/78)

```python
# https://www.acmicpc.net/problem/1697
# 숨바꼭질
# 참고한 블로그: https://data-flower.tistory.com/78
from collections import deque
from sys import stdin

MAX_SIZE = 100_000

input = stdin.readline

DIRECTIONS = [
    lambda x: x + 1,
    lambda x: x - 1,
    lambda x: x * 2
]

N, K = map(int, input().split())
repository = [0] * MAX_SIZE
need_visited = deque([N])

if N >= K:
    print(N - K)
    exit()

while need_visited:
    index = need_visited.popleft()
    print("index:", index, "/ repository:", repository[1:K + 1])

    if repository[K] != 0:
        break

    for direction in DIRECTIONS:
        current = direction(index)
        if 0 <= current <= MAX_SIZE and not repository[current]:
            repository[current] = repository[index] + 1
            need_visited.append(current)

print(repository[K])

```