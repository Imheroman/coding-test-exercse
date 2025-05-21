# 15652번: N과 M (4)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

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
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
```

### 예제 입력 3

```text
3 3
```

### 예제 출력 3

```text
1 1 1
1 1 2
1 1 3
1 2 2
1 2 3
1 3 3
2 2 2
2 2 3
2 3 3
3 3 3
```

## 힌트


## 알고리즘 분류


## 시도

### 시도1(32412KB, 56ms)

DFS를 이용한 조합 함수를 이용하여 구현

```python
# https://www.acmicpc.net/problem/15652
# N과 M (4)
import sys

input = sys.stdin.readline


def combinations_dfs(start, n, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, n + 1):
        repository.append(current)
        combinations_dfs(current, n, size - 1)
        repository.pop()


N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())

combinations_dfs(1, N, M)
```

### 시도2(33432KB, 56ms)

재귀 방법을 이용한 조합 구현

```text
3 3
```

입력이 다음과 같이 주어졌을 때,

원래 `for value in arr:`코드에서 `for value in arr[start -1:]:` 코드를 적용하기 전에 출력이 아래와 같이 나왔는데,
오래 보아도 어떻게 적용을 해야할지 모르겠어서 지피티에게 물어본 후 해결하였다. 

```text
1 1 1
1 1 2
1 1 3
1 2 1
1 2 2
1 2 3
1 3 1
1 3 2
1 3 3
2 2 1
2 2 2
2 2 3
2 3 1
2 3 2
2 3 3
3 3 1
3 3 2
3 3 3
```

```python
# https://www.acmicpc.net/problem/15652
# N과 M (4)
import sys

input = sys.stdin.readline


def combinations(arr, start, size):
    result = []

    if size == 1:
        for value in arr[start -1:]:
            result.append([value])

    elif 1 < size <= len(arr):
        for current in range(start, len(arr) + 1):
            for combinations_result in combinations(arr, current, size - 1):
                result.append([current] + combinations_result)

    return result


N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "3 3".split())
number = [number for number in range(1, N + 1)]

for combination in combinations(number, 1, M):
    print(*combination, sep=' ')
```

### 시도3(33432KB, 48ms)

`itertools`의 `combinations_with_replacement()` 함수를 이용하여 자기 자신을 포함한 조합을 생성하여 작성한 코드

```python
# https://www.acmicpc.net/problem/15652
# N과 M (4)
import sys
import itertools

input = sys.stdin.readline


N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "3 3".split())
number = [number for number in range(1, N + 1)]

for combination in itertools.combinations_with_replacement(number,  M):
    print(*combination, sep=' ')
```

## 정리

