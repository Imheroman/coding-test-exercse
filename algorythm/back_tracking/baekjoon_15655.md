# 15655번: N과 M (6)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. 
N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

## 입출력

### 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제

### 예제 입력 1

```text
3 1
4 5 2
```

### 예제 출력 1

```text
2
4
5
```

### 예제 입력 2

```text
4 2
9 8 7 1
```

### 예제 출력 2

```text
1 7
1 8
1 9
7 8
7 9
8 9
```

### 예제 입력 3

```text
4 4
1231 1232 1233 1234
```

### 예제 출력 3

```text
1231 1232 1233 1234
```

## 힌트

- 백트래킹

## 알고리즘 분류

## 시도

### 시도1(32544kb, 36ms)

`itertools`의 `combinations()`를 이용한 문제 해결

```python
# https://www.acmicpc.net/problem/15655
# N과 M (6)
import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 8 7 1".split())))

for permutation in itertools.combinations(number, M):
    print(*permutation, sep=' ')
```

### 시도2(32412kbm 36ms)

`dfs` 재귀 방법을 이용한 문제 해결

```python
# https://www.acmicpc.net/problem/15655
# N과 M (6)
import sys

input = sys.stdin.readline


def combinations(arr, start, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        if arr[current] not in repository:
            repository.append(arr[current])
            combinations(arr, current + 1, size-1)
            repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 8 7 1".split())))

combinations(number, 0, M)
```

### 시도3

```python

```

## 정리

