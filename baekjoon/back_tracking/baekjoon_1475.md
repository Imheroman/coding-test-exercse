# [1475번: 방 번호](https://www.acmicpc.net/problem/1475)

다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오. (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

## 입출력

### 입력
첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수이다.

### 출력
첫째 줄에 필요한 세트의 개수를 출력한다.

## 예제

### 예제 입력 1

```text
9999
```

### 예제 출력 1

```text
2
```

### 예제 입력 2

```text
122
```

### 예제 출력 2

```text
2
```

### 예제 입력 3

```text
12635
```

### 예제 출력 3

```text
1
```

### 예제 입력 4

```text
888888
```

### 예제 출력 4

```text
6
```

## 알고리즘 분류

- 구현

## 시도

### 시도1(32412kb, 36ms)

0~9까지를 숫자 1세트라고 하고, 총 숫자가 몇 세트가 필요한지를 구하는 문제이다.

숫자가 나온 횟수 중 가장 많은 횟수를 구하면 되지만, 6과 9는 1세트에 2번을 사용할 수 있기 때문에,
9를 6으로 생각하여 문제를 해결했다.

`number_counts[6] = number_counts[6] // 2 + number_counts[6] % 2`은 6과 9가 짝수로 나온다는 보장이 없기 때문에,
홀수인 경우에도 생각을 하여 갯수를 카운트하였다.


```python
# https://www.acmicpc.net/problem/1475
# 방 번호

import sys

input = sys.stdin.readline

numbers = list(map(int, input().rstrip()))
number_counts = {x: 0 for x in range(9)}

for number in numbers:
    if number == 9:
        number_counts[6] += 1
    else:
        number_counts[number] += 1

number_counts[6] = number_counts[6] // 2 + number_counts[6] % 2
print(max(number_counts.values()))
```

## 정리
