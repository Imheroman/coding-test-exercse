# 15657번: N과 M (8)

desN개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.c

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
1 1
1 7
1 8
1 9
7 7
7 8
7 9
8 8
8 9
9 9
```

### 예제 입력 3

```text
4 4
1231 1232 1233 1234
```

### 예제 출력 3

```text
1231 1231 1231 1231
1231 1231 1231 1232
1231 1231 1231 1233
1231 1231 1231 1234
1231 1231 1232 1232
1231 1231 1232 1233
1231 1231 1232 1234
1231 1231 1233 1233
1231 1231 1233 1234
1231 1231 1234 1234
1231 1232 1232 1232
1231 1232 1232 1233
1231 1232 1232 1234
1231 1232 1233 1233
1231 1232 1233 1234
1231 1232 1234 1234
1231 1233 1233 1233
1231 1233 1233 1234
1231 1233 1234 1234
1231 1234 1234 1234
1232 1232 1232 1232
1232 1232 1232 1233
1232 1232 1232 1234
1232 1232 1233 1233
1232 1232 1233 1234
1232 1232 1234 1234
1232 1233 1233 1233
1232 1233 1233 1234
1232 1233 1234 1234
1232 1234 1234 1234
1233 1233 1233 1233
1233 1233 1233 1234
1233 1233 1234 1234
1233 1234 1234 1234
1234 1234 1234 1234
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1

자신의 중복을 허용한 조합 문제

`itertools`를 이용한 해결 

```python
# https://www.acmicpc.net/problem/15657
# N과 M (8)
import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 3, 3
# number = sorted(list(map(int, "1231 1232 1233".split())))

for combination in itertools.combinations_with_replacement(number, M):
    print(*combination, sep=' ')
```

### 시도2

`dfs` 재귀를 이용한 문제 해결

```python
# https://www.acmicpc.net/problem/15657
# N과 M (8)
import sys

input = sys.stdin.readline


def combinations_with_replacement(arr, start, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        repository.append(arr[current])
        combinations_with_replacement(arr, current, size - 1)
        repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 3, 3
# number = sorted(list(map(int, "1231 1232 1233".split())))

combinations_with_replacement(number, 0, M)
```
