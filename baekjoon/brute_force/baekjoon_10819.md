# $10891번: 차이를 최대로

N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

```text
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
```

## 입출력

### 입력
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

### 출력
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

## 예제

### 예제 입력 1

```text
6
20 1 15 8 4 10
```

### 예제 출력 1

```text
62
```

## 시도

### 시도1

이 문제를 통해서 브루트 포스라는 알고리즘을 처음 접해보았다.

처음 문제를 접근할 때, 최댓값과 최솟값을 대조하여 해결하려고 했는데, 이는 아무리 봐도 틀린 방법이였다.

알고리즘 분류를 확인하였으나, 브루트 포스 알고리즘과 백트래킹이라는 알고리즘을 모르겠어서 검색했다.

다른 사람들도 최댓값과 최솟값을 먼저 비교하였으나, 오답인 걸 알고 많이 고민했던 흔적이 있었고,
모든 순열을 구할 수 있는 `from itertools import permutations`을 알게 되었다.

(결국 중간 값을 양 끝에 두고, 최댓값과 최솟값을 번갈아 두어야 문제가 해결됨)

해당 라이브러리를 이용하여 문제를 해결한 코드

```python
# https://www.acmicpc.net/problem/10819
# 차이를 최대로
import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# N = 6
# A = list(map(int, "20 1 15 8 4 10".split()))

answer = 0
for permutation in permutations(A):
    current_max = 0
    for i in range(1, N):
        current_max += abs(permutation[i - 1] - permutation[i])
    if current_max > answer:
        answer = current_max

print(answer)

```

## 정리

브루트 포스 알고리즘이란 가능한 모든 경우의 수를 확인하는 알고리즘이다. 
