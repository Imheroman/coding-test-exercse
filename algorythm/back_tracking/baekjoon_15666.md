# 15664번: N과 M (11)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

## 입출력

### 입력

첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 
입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

### 출력

한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.

## 예제

### 예제 입력 1

```text
3 1
4 4 2
```

### 예제 출력 1

```text
2
4
```

### 예제 입력 2

```text
4 2
9 7 9 1
```

### 예제 출력 2

```text
1 1
1 7
1 9
7 7
7 9
9 9
```

### 예제 입력 3

```text
4 4
1 1 2 2
```

### 예제 출력 3

```text
1 1 1 1
1 1 1 2
1 1 2 2
1 2 2 2
2 2 2 2
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1(33432kb, 296ms)

이전과 같이 `itertools`의 `combinations_with_replacement`를 이용하여 중복 조합을 만들었고,
`answer`에 답을 저장하여 중복되지 않는 것으로 출력하였다.

```python
# https://www.acmicpc.net/problem/15666
# N과 M (12)
import sys
import itertools

input = sys.stdin.readline


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(list(map(int, "1 1 2 2".split())))
answer = []

for combination in itertools.combinations_with_replacement(number, M):
    if combination not in answer:
        answer.append(combination)
        print(*combination, sep=' ')
# combinations(number, 0, M)
```

### 시도2(32412kb, 40ms)

[이전 문제(백준 15665번)](./baekjoon_15665.md)에서 깨닫고 배운 내용으로 set으로만 변경하여 문제 해결

```python
# https://www.acmicpc.net/problem/15666
# N과 M (12)
import sys
import itertools

input = sys.stdin.readline


N, M = map(int, input().split())
number = sorted(set(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(set(map(int, "1 1 2 2".split())))

for combination in itertools.combinations_with_replacement(number, M):
    print(*combination, sep=' ')
```

### 시도3(32412kb, 40ms)

직접 중복을 허용한 조합 수열을 구현하여 해결

```python
# https://www.acmicpc.net/problem/15666
# N과 M (12)
import sys

input = sys.stdin.readline


def combinations_with_replace(arr, start, size, repository=[]):
    # print("repository:", repository, ", size:", size)
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        repository.append(arr[current])
        combinations_with_replace(arr, current, size - 1)
        repository.pop()


N, M = map(int, input().split())
number = sorted(set(map(int, input().split())))
# N, M = 3, 1
# number = sorted(set(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(set(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(set(map(int, "1 1 2 2".split())))

combinations_with_replace(number, 0, M)
```


### 시도4()

```python
```


### 시도5()

```python
```

