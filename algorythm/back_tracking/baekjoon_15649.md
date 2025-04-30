# 15649번: N과 M (1)

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

## 입출력

### 입력

첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

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
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3
```

### 예제 입력 3

```text
4 4
```

### 예제 출력 3

```text
1 2 3 4
1 2 4 3
1 3 2 4
1 3 4 2
1 4 2 3
1 4 3 2
2 1 3 4
2 1 4 3
2 3 1 4
2 3 4 1
2 4 1 3
2 4 3 1
3 1 2 4
3 1 4 2
3 2 1 4
3 2 4 1
3 4 1 2
3 4 2 1
4 1 2 3
4 1 3 2
4 2 1 3
4 2 3 1
4 3 1 2
4 3 2 1
```

## 알고리즘 분류

- 백트래킹

## 시도

### 시도1 (33432KB, 132ms)

전에 수열과 관련된 문제를 풀었기 때문에 `itertools`의 `permutations` 함수를 이용하여 어렵지 않게 해결할 수 있었다.

```python
# https://www.acmicpc.net/problem/15649
# N과 M (1)
import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
# N, M = map(int, "4 4".split())

permutation_list = permutations([i for i in range(1, N + 1)], M)
for permutation in permutation_list:
    print(*permutation, sep=' ')

```

### 시도2(38552KB, 208ms)

라이브러리를 사용하지 않고, 재귀를 이용하여 문제를 해결해보려 다시 해결해보았다.

[allkites](https://yangnyang.tistory.com/14)님의 블로그에 작성된 코드를 참고하여 작성한 재귀를 이용한 순열 생성 함수

```python
# https://www.acmicpc.net/problem/15649
# N과 M (1)
import sys

input = sys.stdin.readline


def permutations(arr, size):
    result = []

    if size == 1:
        for current in arr:
            result.append([current])

    elif 1 < size <= len(arr):
        for current in arr:
            copy_arr = [i for i in arr]  # arr 복사(다음 순열을 구하기 위해)
            copy_arr.remove(current)  # 본인을 제외한 전체 array가 됨
            for permutation_result in permutations(copy_arr, size - 1):
                # 재귀를 돌면서 계속해서 본인을 제외한 순열을 만들고, Top-Down 방식으로 마지막 size가 1이 됐을 때
                # result가 return 돼서 본인을 제외했던 순열 리스트가 나온다. 본인과 합하여 새로운 순열들을 1개씩 생성한다.
                result.append([current] + permutation_result)  # 제외된 list 값에 생성된 list에 추가함

    return result


N, M = map(int, input().split())

numbers = [i for i in range(1, N + 1)]
for permutation in permutations(numbers, M):
    print(*permutation, sep=' ')
```

### 시도3(32412KB, 184ms)

다른 사람들의 풀이법을 찾아보던 중 [Jiwon_C](https://jiwon-coding.tistory.com/22)님의 블로그를 찾아보게 되었다.

**Jiwon_C**님의 방식은 `list`를 계속 return하는 것이 아니라, `repository`를 이용해서 숫자를 저장하고,
일정 크기가 됐을 때 print하는 방법이였다.

이 코드가 더 간결하고 읽기 편한 것 같다.

```python
# https://www.acmicpc.net/problem/15649
# N과 M (1)
import sys

input = sys.stdin.readline


def permutations(n, size, repository=[]):
    if size == 0:
        print(*repository, sep=' ')
        return

    for current in range(1, n + 1):
        if current not in repository:
            repository.append(current)
            permutations(n, size - 1)
            repository.pop()


N, M = map(int, input().split())
# N, M = map(int, "3 1".split())
# N, M = map(int, "4 2".split())
permutations(N, M)
```

## 정리

알고리즘에는 여러 접근법이 있어서 재밌다.
