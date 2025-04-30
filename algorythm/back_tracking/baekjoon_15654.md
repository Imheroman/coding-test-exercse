# 15654번: N과 M (5)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

- N개의 자연수 중에서 M개를 고른 수열

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
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8
```

### 예제 입력 3

```text
4 4
1231 1232 1233 1234
```

### 예제 출력 3

```text
1231 1232 1233 1234
1231 1232 1234 1233
1231 1233 1232 1234
1231 1233 1234 1232
1231 1234 1232 1233
1231 1234 1233 1232
1232 1231 1233 1234
1232 1231 1234 1233
1232 1233 1231 1234
1232 1233 1234 1231
1232 1234 1231 1233
1232 1234 1233 1231
1233 1231 1232 1234
1233 1231 1234 1232
1233 1232 1231 1234
1233 1232 1234 1231
1233 1234 1231 1232
1233 1234 1232 1231
1234 1231 1232 1233
1234 1231 1233 1232
1234 1232 1231 1233
1234 1232 1233 1231
1234 1233 1231 1232
1234 1233 1232 1231
```

## 힌트

- 백트래킹

## 알고리즘 분류

## 시도

### 시도1(32412kb, 118ms)

dfs 재귀 방식을 이용한 문제 해결 

```python
# https://www.acmicpc.net/problem/15654
# N과 M (5)
import sys

input = sys.stdin.readline


def permutations(arr, size, repository=[]):  # 1, 7, 8, 9
    # print(f"size: {size}, repository: {repository}")
    if size == 0:
        print(*repository, sep=' ')
        return

    elif 0 < size <= len(arr):
        for current in arr:
            if current not in repository:
                repository.append(current)
                permutations(arr, size - 1)
                repository.pop()


N, M = map(int, input().split())
permutation_matrix = sorted(list(map(int, input().split())))
# N, M = 3, 1
# permutation_matrix = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# permutation_matrix = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 4, 4
# permutation_matrix = sorted(list(map(int, "1231 1232 1233 1234".split())))

permutations(permutation_matrix, M)
```

### 시도2

`itertools`의 `permutation` 함수를 이용한 문제 해결 

```python
# https://www.acmicpc.net/problem/15654
# N과 M (5)
import sys
import itertools

input = sys.stdin.readline


N, M = map(int, input().split())
permutation_matrix = sorted(list(map(int, input().split())))
# N, M = 3, 1
# permutation_matrix = sorted(list(map(int, "4 5 2".split())))
# N, M = 4, 2
# permutation_matrix = sorted(list(map(int, "9 8 7 1".split())))
# N, M = 4, 4
# permutation_matrix = sorted(list(map(int, "1231 1232 1233 1234".split())))

for permutation in itertools.permutations(permutation_matrix, M):
    print(*permutation, sep=' ')

```

## 정리

