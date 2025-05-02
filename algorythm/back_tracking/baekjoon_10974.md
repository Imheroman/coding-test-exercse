# 10974번: 모든 순열

N이 주어졌을 때, 1부터 N까지의 수로 이루어진 순열을 사전순으로 출력하는 프로그램을 작성하시오.

## 입출력

### 입력
첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다. 

### 출력
첫째 줄부터 N!개의 줄에 걸쳐서 모든 순열을 사전순으로 출력한다.

## 예제

### 예제 입력 1

```text
3
```

### 예제 출력 1

```text
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

## 알고리즘 분류

- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(33432kb, 132ms)

이전에 백트래킹 문제들을 모두 수열로 풀어서 그런지 쉽게 접근이 가능했다.

처음 접근은 그래도 쉽게 `itertools.permutations()`를 이용해 해결했다.

```python
import sys
import itertools

input = sys.stdin.readline

N = int(input())
number = [num for num in range(1, N + 1)]

for permutation in itertools.permutations(number, N):
    print(*permutation)
```

### 시도2(32412kb, 172ms)

재귀함수를 직접 구현하여 작성한 정답  

```python
import sys

input = sys.stdin.readline


def permutations(arr, size, repository=[]):
    if size == 0:
        print(*repository)
        return

    for num in arr:
        if num not in repository:
            repository.append(num)
            permutations(arr, size - 1)
            repository.pop()


N = int(input())
number = [num for num in range(1, N + 1)]
permutations(number, N)
```

## 정리

