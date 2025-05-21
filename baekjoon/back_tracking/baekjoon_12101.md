# [12101번: 1, 2, 3 더하기 2](https://www.acmicpc.net/problem/12101)

정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
- 1+3
- 3+1

이를 사전순으로 정렬하면 다음과 같이 된다.

1. 1+1+1+1
2. 1+1+2
3. 1+2+1
4. 1+3
5. 2+1+1
6. 2+2
7. 3+1

정수 n과 k가 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법 중에서 k번째로 오는 식을 구하는 프로그램을 작성하시오.

## 입출력

### 입력

첫째 줄에 정수 n과 k가 주어진다. n은 양수이며 11보다 작고, k는 231-1보다 작거나 같은 자연수이다.

### 출력

n을 1, 2, 3의 합으로 나타내는 방법 중에서 사전 순으로 k번째에 오는 것을 출력한다. k번째 오는 식이 없는 경우에는 -1을 출력한다.

## 예제

### 예제 입력 1

```text
4 3
```

### 예제 출력 1

```text
1+2+1
```

### 예제 입력 2

```text
4 5
```

### 예제 출력 2

```text
2+1+1
```

### 예제 입력 3

```text
4 7
```

### 예제 출력 3

```text
3+1
```

### 예제 입력 3

```text
4 8
```

### 예제 출력 3

```text
-1
```

## 알고리즘 분류

- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(32412kb, 68ms)

1, 2, 3의 합으로 n을 만드는데, 사전순으로 정렬된 리스트의 k번째 수열을 출력한다.

1, 2, 3만 만들면 되기 때문에 1, 2, 3으로 중복을 허용하는 수열을 만들어서 합이 4인 경우 리스트에 저장해주었다.

```python
# https://www.acmicpc.net/problem/12101
# 1, 2, 3 더하기 2
import sys
import itertools

input = sys.stdin.readline

NUMBERS = [1, 2, 3]

n, k = map(int, input().split())
# n, k = 4, 3
# n, k = 4, 5
# n, k = 4, 7
# n, k = 4, 8

answer = []
for digit in range(n, 0, -1):
    for combination in itertools.product(NUMBERS, repeat=digit):
        if sum(combination) == n:
            answer.append(combination)

if len(answer) < k:
    print(-1)
else:
    print(*sorted(answer)[k - 1], sep='+')

```