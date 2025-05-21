# 1182번: 부분 수열의 합

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

## 입출력

### 입력
첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 
주어지는 정수의 절댓값은 100,000을 넘지 않는다.

### 출력
첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

## 예제

### 예제 입력 1

```text
5 0
-7 -3 -2 5 8
```

### 예제 출력 1

```text
1
```

## 알고리즘 분류

- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(32412kb, 368ms)

원소를 다 더한 값이 S가 되는 경우의 수를 찾으라고 하였고, 
예제 1에 대해서 출력이 1이 나왔으니, 수열이 아닌 조합을 찾는 것으로 파악하고 문제를 해결하였다.

처음에는 문제를 빠르게 해결하기 위해 `itertools.combinations()`을 이용하여 문제를 해결했다.

```python
import sys
import itertools

input = sys.stdin.readline

N, S = map(int, input().split())
number = list(map(int, input().split()))

answer = 0
for size in range(1, N + 1):
    for combination in itertools.combinations(number, size):
        if sum(combination) == S:
            answer += 1

print(answer)
```

### 시도2(32412kb, 2588ms)

직접 `combinations()`을 이용하여 문제를 해결한 코드

```python
import sys

input = sys.stdin.readline


def combinations(arr, start, size, target, repository=[]):
    result = 0

    if size == 0:
        if sum(repository) == target:
            result += 1
        return result

    for current in range(start, len(arr)):
        repository.append(arr[current])
        result += combinations(arr, current + 1, size - 1, target, repository)
        repository.pop()

    return result


N, S = map(int, input().split())
number = list(map(int, input().split()))

answer = 0
for index in range(1, N + 1):
    answer += combinations(number, 0, index, S)

print(answer)
```

## 정리
