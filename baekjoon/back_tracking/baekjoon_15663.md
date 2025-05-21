# 15663번: N과 M (11)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

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
7 1
7 9
9 1
9 7
9 9
```

### 예제 입력 3

```text
4 4
1 1 1 1
```

### 예제 출력 3

```text
1 1 1 1
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1

그림으로 그려봐도 방법을 모르겠어서 일단 가장 쉽게 접근할 수 있는
`answer`에 답을 저장하며 작성한 코드를 제출해봤지만 역시나 시간 초과 

```python
import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))

answer = []
for permutation in itertools.permutations(number, M):
    if permutation not in answer:
        answer.append(permutation)
        print(*permutation, sep=' ')
```

### 시도2(37024kb, 104ms)

약 1시간은 고민을 해봤는데, 모르겠어서 결국 `set()`을 이용해서 다시 풀어보기로 하였고, 정답이 인정됐다.

```python
# https://www.acmicpc.net/problem/15663
# N과 M (11)
import sys
import itertools

input = sys.stdin.readline

N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))

answer = set()
for permutation in itertools.permutations(number, M):
    answer.add(permutation)

for value in answer:
    print(*value, sep=' ')
```

### 시도3(37024kb, 120ms)

내장 함수 `itertools.permutations` 대신 직접 수열 함수를 구현하여 해결

```python
# https://www.acmicpc.net/problem/15663
# N과 M (11)
import sys
import itertools

input = sys.stdin.readline


def permutations(arr, size, answer, repository=[]):
    if size == 0:
        # print(*repository, sep=' ')
        answer.add(tuple(repository))
        return

    for current in range(len(arr)):
        copy_arr = arr.copy()
        copy_arr.remove(arr[current])
        repository.append(arr[current])
        # permutations(arr, size-1, answer)
        permutations(copy_arr, size-1, answer)
        repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))
# number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(list(map(int, "1 1 1 1".split())))

ans = set()
permutations(number, M, ans)

for value in sorted(ans):
    print(*value, sep=' ')
```

### 시도4(32544kb, 88ms)

[Alan_Kim](https://thought-process-ing.tistory.com/87)님 블로그에서 참고한 코드

```python
# https://www.acmicpc.net/problem/15663
# N과 M (11)
import sys
import itertools

input = sys.stdin.readline


def permutations(arr, size, visited, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    pre = -1
    for current in range(len(arr)):
        if arr[current] != pre and not visited[current]:
            pre = arr[current]
            visited[current] = True
            repository.append(arr[current])
            permutations(arr, size - 1, visited)
            visited[current] = False
            repository.pop()


N, M = map(int, input().split())
number = sorted(list(map(int, input().split())))
# N, M = 3, 1
# number = sorted(list(map(int, "4 4 2".split())))
# N, M = 4, 2
# number = sorted(list(map(int, "9 7 9 1".split())))
# N, M = 4, 4
# number = sorted(list(map(int, "1 1 1 1".split())))

v = [False] * N
permutations(number, M, v)
```
