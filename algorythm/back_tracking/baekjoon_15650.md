# 15649번: N과 M (2)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

## 입출력

### 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제

### 예제 입력 1

```text
3 1
```

### 예제 출력 1

```text
1
2
3
```

### 예제 입력 2

```text
4 2
```

### 예제 출력 2

```text
1 2
1 3
1 4
2 3
2 4
3 4
```

### 예제 입력 3

```text
4 4
```

### 예제 출력 3

```text
1 2 3 4
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1 (32412KB, 36ms)

수열의 재귀 함수를 공부할 때 재귀 함수도 같이 공부했었기 때문에 쉭베 풀 수 있었다.

코드에 대한 이해는 됐지만, 시간이 지나도 잊어버리지 않도록 잘 기억해야할 것 같다.

```python
# https://www.acmicpc.net/problem/15650
# N과 M (2)
import sys

input = sys.stdin.readline


def combinations(arr, size):
    result = []

    if size == 1:
        for value in arr:
            result.append([value])

    arr_size = len(arr)
    if 1 < size <= arr_size:
        for current in range(arr_size - size + 1):
            for combination_result in combinations(arr[current + 1:], size - 1):
                result.append([arr[current]] + combination_result)

    return result


N, M = map(int, input().split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())
numbers = [i for i in range(1, N + 1)]

for combination in combinations(numbers, M):
    print(*combination, sep=' ')
```

### 시도2 (32412KB, 36ms)

이번엔 itertools 내장 함수를 이용해서 문제를 해결해보았다.

신기하게도 메모리 소모와 시간은 동일하다.

```python
# https://www.acmicpc.net/problem/15650
# N과 M (2)
import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())
numbers = [i for i in range(1, N + 1)]

for combination in combinations(numbers, M):
    print(*combination, sep=' ')
```

### 시도3 (32412KB, 32ms)

[Jiwon_C](https://jiwon-coding.tistory.com/22)님의 블로그를 보고 참고한 조합 방법2

```python
# https://www.acmicpc.net/problem/15650
# N과 M (2)
import sys

input = sys.stdin.readline


def combinations(start, n, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')

    for current in range(start, n + 1):
        if current not in repository:
            repository.append(current)
            combinations(current + 1, n, size - 1)
            repository.pop()


N, M = map(int, input().split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())

combinations(1, N, M)
```

## 정리

재귀는 어렵다.
