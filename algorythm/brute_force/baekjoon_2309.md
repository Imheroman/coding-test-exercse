# ${number}번: title

왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.

## 입출력

### 입력
아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어진다. 주어지는 키는 100을 넘지 않는 자연수이며, 아홉 난쟁이의 키는 모두 다르며, 가능한 정답이 여러 가지인 경우에는 아무거나 출력한다.

### 출력
일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.

## 예제

### 예제 입력 1

```text
20
7
23
19
10
15
25
8
13
```

### 예제 출력 1

```text
7
8
10
13
19
20
23
```

## 시도

### 시도1(정답)

이전 문제로 [백준10819 문제(차이를 최대로)](./baekjoon_10819.py)를 풀어서 어렵지 않게 해결했다.

모든 순열을 구해서, 키의 합이 100이 되면 그 값을 출력했다.

```python
# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
import sys
from itertools import permutations

input = sys.stdin.readline

N = 9
TARGET_DWARF_NUMBER = 7
TARGET_HEIGHT = 100
dwarfs = [int(input()) for _ in range(N)]
# dwarfs = [20, 7, 23, 19, 10, 15, 25, 8, 13]

for dwarf in permutations(dwarfs, TARGET_DWARF_NUMBER):
    if sum(dwarf) == TARGET_HEIGHT:
        print(*sorted(dwarf), sep="\n")
        break
```

### 시도2

문제를 해결하고 [유지광이님의 티스토리 블로그](https://ji-gwang.tistory.com/244)를 확인해 보니 조합을 사용하여 문제를 해결하였다. 

순열은 순서가 중요한 리스트이고, 조합은 순서가 없는 리스트이기 때문에 중복이 없다.

따라서 이 문제는 순열보다는 조합 라이브러리를 사용한 코드가 더 적합한 해결 방법이라고 생각한다. 

```python
# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
import sys
from itertools import combinations

input = sys.stdin.readline

N = 9
TARGET_DWARF_NUMBER = 7
TARGET_HEIGHT = 100
dwarfs = [int(input()) for _ in range(N)]
# dwarfs = [20, 7, 23, 19, 10, 15, 25, 8, 13]

for dwarf in combinations(dwarfs, TARGET_DWARF_NUMBER):
    if sum(dwarf) == TARGET_HEIGHT:
        print(*sorted(dwarf), sep="\n")
        break

```

### 시도3

**유지광이님의 티스토리 블로그**를 보고 풀었을 때, 라이브러리 없이 for 반복문만을 이용하여 문제를 풀었던 것을 확인하고 나도 풀어보고 싶어서 도전하였다.

나는 계속 7개의 숫자를 어떻게 정해야 하나 고민하다 문제 해결이 안 돼서 블로그를 다시 확인하였지만, 
**유지광이**님은 단순히 숫자 2개를 뺐다.

```python
# https://www.acmicpc.net/problem/2309
# 일곱 난쟁이
import sys

input = sys.stdin.readline

N = 9
TARGET_DWARF_NUMBER = 7
TARGET_HEIGHT = 100
dwarfs = sorted([int(input()) for _ in range(N)])
# dwarfs = sorted([20, 7, 23, 19, 10, 15, 25, 8, 13])

print(dwarfs)
current_sum = sum(dwarfs)
for i in range(N):
    for j in range(i + 1, N):
        if current_sum - dwarfs[i] - dwarfs[j] == TARGET_HEIGHT:
            for index in range(N):
                if not (index == i or index == j):
                    print(dwarfs[index])
            exit()
```

## 정리

다양한 방법으로 문제를 접근해보고, 
9개에서 7개를 정하는 방법은 7개를 선택하는 방법도 있지만 2개를 빼는 방법도 있다.
