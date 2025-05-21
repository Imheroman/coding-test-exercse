# [2529번: 부등호](https://www.acmicpc.net/problem/2529)

두 종류의 부등호 기호 ‘<’와 ‘>’가 k개 나열된 순서열 A가 있다. 우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서 모든 부등호 관계를 만족시키려고 한다. 예를 들어, 제시된 부등호 순서열 A가 다음과 같다고 하자. 

`A ⇒ < < < > < < > < >`

부등호 기호 앞뒤에 넣을 수 있는 숫자는 0부터 9까지의 정수이며 선택된 숫자는 모두 달라야 한다. 아래는 부등호 순서열 A를 만족시키는 한 예이다. 

`3 < 4 < 5 < 6 > 1 < 2 < 8 > 7 < 9 > 0`

이 상황에서 부등호 기호를 제거한 뒤, 숫자를 모두 붙이면 하나의 수를 만들 수 있는데 이 수를 주어진 부등호 관계를 만족시키는 정수라고 한다. 그런데 주어진 부등호 관계를 만족하는 정수는 하나 이상 존재한다. 예를 들어 3456128790 뿐만 아니라 5689023174도 아래와 같이 부등호 관계 A를 만족시킨다. 

`5 < 6 < 8 < 9 > 0 < 2 < 3 > 1 < 7 > 4`

여러분은 제시된 k개의 부등호 순서를 만족하는 (k+1)자리의 정수 중에서 최댓값과 최솟값을 찾아야 한다. 앞서 설명한 대로 각 부등호의 앞뒤에 들어가는 숫자는 { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 }중에서 선택해야 하며 선택된 숫자는 모두 달라야 한다. 

## 입출력

### 입력
첫 줄에 부등호 문자의 개수를 나타내는 정수 k가 주어진다. 
그 다음 줄에는 k개의 부등호 기호가 하나의 공백을 두고 한 줄에 모두 제시된다. k의 범위는 2 ≤ k ≤ 9 이다. 

### 출력
여러분은 제시된 부등호 관계를 만족하는 k+1 자리의 최대, 최소 정수를 첫째 줄과 둘째 줄에 각각 출력해야 한다. 
단 아래 예(1)과 같이 첫 자리가 0인 경우도 정수에 포함되어야 한다. 
모든 입력에 답은 항상 존재하며 출력 정수는 하나의 문자열이 되도록 해야 한다.

## 예제

### 예제 입력 1

```text
2
< >
```

### 예제 출력 1

```text
897
021
```

### 예제 입력 2

```text
9
> < < < > > > < <
```

### 예제 출력 2

```text
9567843012
1023765489
```

## 알고리즘 분류

- 브루트포스 알고리즘
- 백트래킹

## 시도

### 시도1(35480kb, 2992ms)

0 ~ 9 까지 모든 수를 구해야 하니, 부등호의 수 + 1개의 수를 가진 자신이 중복되지 않은 수열을 만들어서 값을 직접 비교하였다.

이미 수열을 다 만들고, 그 값을 다시 비교하다 보니 시간이 오래 측정되는 것 같다.

빠르게 구현하기 위해 `itertoos.permutations()`를 이용하여 문제를 해결했다.


```python
# https://www.acmicpc.net/problem/2529
# 부등호
import sys
import itertools

input = sys.stdin.readline

K = int(input())
inequalities = list(input().split())
# K = 2
# inequalities = ["<", ">"]
# K = 9
# inequalities = [">", "<", "<", "<", ">", ">", ">", "<", "<"]
numbers = [x for x in range(10)]

answer = []
for permutation in itertools.permutations(numbers, K + 1):
    flag = True
    for current in range(len(inequalities)):
        num1, num2 = permutation[current], permutation[current + 1]
        inequality = inequalities[current]
        if inequality == ">":
            flag = num1 > num2
        else:
            flag = num1 < num2

        if not flag:
            break

    if flag:
        answer.append(permutation)

print(*max(answer), sep='')
print(*min(answer), sep='')
```

### 시도2

```python

```

### 시도3

```python

```

### 시도4

```python

```

## 정리

