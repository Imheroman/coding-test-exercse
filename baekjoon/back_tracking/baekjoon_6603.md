# 6603번: 로또

독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.

로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

## 입출력

### 입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스는 한 줄로 이루어져 있다. 첫 번째 수는 k (6 < k < 13)이고, 다음 k개 수는 집합 S에 포함되는 수이다. S의 원소는 오름차순으로 주어진다.

입력의 마지막 줄에는 0이 하나 주어진다. 

### 출력
각 테스트 케이스마다 수를 고르는 모든 방법을 출력한다. 이때, 사전 순으로 출력한다.

각 테스트 케이스 사이에는 빈 줄을 하나 출력한다.

## 예제

### 예제 입력 1

```text
7 1 2 3 4 5 6 7
8 1 2 3 5 8 13 21 34
0
```

### 예제 출력 1

```text
1 2 3 4 5 6
1 2 3 4 5 7
1 2 3 4 6 7
1 2 3 5 6 7
1 2 4 5 6 7
1 3 4 5 6 7
2 3 4 5 6 7

1 2 3 5 8 13
1 2 3 5 8 21
1 2 3 5 8 34
1 2 3 5 13 21
1 2 3 5 13 34
1 2 3 5 21 34
1 2 3 8 13 21
1 2 3 8 13 34
1 2 3 8 21 34
1 2 3 13 21 34
1 2 5 8 13 21
1 2 5 8 13 34
1 2 5 8 21 34
1 2 5 13 21 34
1 2 8 13 21 34
1 3 5 8 13 21
1 3 5 8 13 34
1 3 5 8 21 34
1 3 5 13 21 34
1 3 8 13 21 34
1 5 8 13 21 34
2 3 5 8 13 21
2 3 5 8 13 34
2 3 5 8 21 34
2 3 5 13 21 34
2 3 8 13 21 34
2 5 8 13 21 34
3 5 8 13 21 34
```

## 알고리즘 분류

- 수학
- 조합론
- 백트래킹
- 재귀

## 시도

### 시도1(32412kb, 36ms)

`8개(K 크기) 중 6개(로또 크기)를 고르는 경우 총 28가지`라고 문제에 언급이 되었고, 
이는 조합의 공식으로 얻을 수 있는 수이다.

또한 집합(중복이 없음)을 구하는 것이니 이 문제는 조합을 이용하여 로또 번호를 출력하는 문제이다.

처음에는 빨리 해결할 수 있도록 `itertoos.combinations()`를 이용하여 문제를 해결했다.

```python
# https://www.acmicpc.net/problem/6603
# 로또
import sys
import itertools

input = sys.stdin.readline
LOTTO_SIZE = 6

while True:
    line = input().rstrip()

    if line == '0':
        break

    number = list(map(int, line.split()))
    k = number.pop(0)
    number.sort()

    for combination in itertools.combinations(number, LOTTO_SIZE):
        print(*combination)

    print()
```

### 시도2(32412kb, 36ms)

직접 `combinations()`를 구현하여 해결

```python
# https://www.acmicpc.net/problem/6603
# 로또
import sys


def combinations(arr, start, size, repository=[]):
    if size == 0:
        print(*repository)
        return

    for current in range(start, len(arr)):
        if arr[current] not in repository:
            repository.append(arr[current])
            combinations(arr, current + 1, size - 1)
            repository.pop()


input = sys.stdin.readline
LOTTO_SIZE = 6

while True:
    line = input().rstrip()

    if line == '0':
        break

    number = list(map(int, line.split()))
    k = number.pop(0)
    number.sort()

    combinations(number, 0, LOTTO_SIZE)
    print()
```

### 시도3

```python

```

### 시도4

```python

```

## 정리

