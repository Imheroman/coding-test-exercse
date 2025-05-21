# 15649번: N과 M (3)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.

## 입출력

### 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

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
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
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
1 2 1
1 2 2
1 2 3
1 3 1
1 3 2
1 3 3
2 1 1
2 1 2
2 1 3
2 2 1
2 2 2
2 2 3
2 3 1
2 3 2
2 3 3
3 1 1
3 1 2
3 1 3
3 2 1
3 2 2
3 2 3
3 3 1
3 3 2
3 3 3
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1 (158004KB, 3504ms)

수열 함수를 직접 구현할 수 있고, 이해할 수 있으면 구현할 수 있는 문제인 것 같다. 

원래의 수열 함수는 본인을 제거하고 재귀로 들어가기 때문에 같은 수가 중복되지 않는다.
하지만, 재귀 함수로 들어가기 전에 본인을 제거하지 않으면 중복이 발생하여 문제를 해결할 수 있다.

```python
# https://www.acmicpc.net/problem/15651
# N과 M (3)
import sys

input = sys.stdin.readline


def permutations(arr, size):
    result = []
    arr_size = len(arr)

    if size == 1:
        for value in arr:
            result.append([value])

    elif 1 < size <= arr_size:
        for current in arr:
            for permutations_result in permutations(arr, size-1):
                result.append([current] + permutations_result)

    return result


N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())
numbers = [i for i in range(1, N + 1)]

for permutation in permutations(numbers, M):
    print(*permutation, sep=' ')
```

### 시도2 (32412KB, 1888ms)

[Jiwon_C](https://jiwon-coding.tistory.com/21)님의 수열 함수 코드를 보고, 이해한 후 작성해본 코드

list를 다루며 수열을 다루는 함수보다 훨씬 빠르다.

```python
# https://www.acmicpc.net/problem/15651
# N과 M (3)
import sys

input = sys.stdin.readline


def permutations(arr, size):
    result = []
    arr_size = len(arr)

    if size == 1:
        for value in arr:
            result.append([value])

    elif 1 < size <= arr_size:
        for current in arr:
            for permutations_result in permutations(arr, size-1):
                result.append([current] + permutations_result)

    return result


N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 3".split())
# N, M = map(int, "4 4".split())
numbers = [i for i in range(1, N + 1)]

for permutation in permutations(numbers, M):
    print(*permutation, sep=' ')
```


## 정리
