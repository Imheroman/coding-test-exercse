# [1038번: 감소하는 수](https://www.acmicpc.net/problem/1038)

음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는
프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

## 입출력

### 입력

첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

### 출력

첫째 줄에 N번째 감소하는 수를 출력한다.

## 예제

### 예제 입력 1

```text
18
```

### 예제 출력 1

```text
42
```

### 예제 입력 2

```text
0
```

### 예제 출력 2

```text
0
```

### 예제 입력 3

```text
500000
```

### 예제 출력 3

```text
-1
```

## 알고리즘 분류

- 백트래킹
- 브루트포스 알고리즘

## 시도

### 시도1(32412kb, 36ms)

[sugyeong_hh](https://velog.io/@sugyeonghh/%EB%B0%B1%EC%A4%80-1038-%EA%B0%90%EC%86%8C%ED%95%98%EB%8A%94-%EC%88%98Python)
님의 블로그를 보고 작성한 코드이다.

**sugyeong_hh**님도 다른 분의 블로그를 보고 작성한 글이지만, 코드가 간단하고 이해하기도 괜찮았다.

조합을 이용해서 digit 자리 수를 만들고, (보통 작은 수에서 큰 수로 조합을 만든다.)
조합을 뒤집어 `감소하는 수`로 만든다.

결과값을 저장해서, 필요한 N의 값을 출력한다.

```python
# https://www.acmicpc.net/problem/1038
# 감소하는 수
import sys
import itertools

input = sys.stdin.readline

N = int(input())
# N = 18
# N = 0
# N = 1000000

answer = []
for digit in range(1, 11):  # 최대는 9876543210 총 10자리이기 때문에
    for combination in itertools.combinations(range(10), digit):
        num = ''.join(list(map(str, reversed(list(combination)))))
        decrement_number = reversed(list(combination))
        answer.append(int("".join(list(map(str, decrement_number)))))

print()
answer.sort()
if N > len(answer):
    print(-1)
else:
    print(answer[N])

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

