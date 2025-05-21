# 15664번: N과 M (10)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 비내림차순이어야 한다.
  - 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

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
1 7
1 9
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
1 1 2 2
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1(32412kb, 36ms)

조합을 만들라는 문제이며, 중복되는 숫자에 대해서는 생성하지 않는 다는 걸로 이해했다.

처음에는 `Set`으로 중복되는 숫자를 없애버릴까 생각을 했지만,

```text
4 4
1 1 2 2
```

의 출력 결과로 

```text
1 1 2 2
```

가 나오는 것을 보고, 중복되는 숫자를 없애면 정답을 맞출 수 없다고 생각이 됐다.

어떻게 하지 고민하다가 가장 간단하게 `answer` 이라는 리스트를 만들어서 출력한 적 없는 조합일 시
출력하는 걸로 문제를 해결해보았더니 정답이였다.

`N`, `M`이 최대 8까지만 주어지기 떄문에 리스트에 저장하는 방식으로 풀이할 수 있었던 것 같다.

```python
# https://www.acmicpc.net/problem/15664
# N과 M (10)
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

for combination in itertools.combinations(number, M):
    if combination not in answer:
        answer.append(combination)
        print(*combination, sep=' ')
```

### 시도2(32412kb, 36ms)

`dfs` 재귀 함수를 만들어 해결

```python
# https://www.acmicpc.net/problem/15664
# N과 M (10)
import sys

input = sys.stdin.readline


def combinations(arr, start, size, repository=[], answer=[]):
    if size == 0 and repository not in answer:
        answer.append(repository.copy())
        print(*repository, sep=' ')
        return

    for current in range(start, len(arr)):
        repository.append(arr[current])
        combinations(arr, current + 1, size - 1)
        repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(list(map(int, "1 1 2 2".split())))

combinations(number, 0, M)
```