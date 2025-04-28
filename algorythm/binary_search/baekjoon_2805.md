# 2805번: 나무 자르기

상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 
정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.

목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 
높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 
따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 
예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

## 입출력

### 입력
첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)

둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 
높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

### 출력
적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

## 예제

### 예제 입력 1

```text
4 7
20 15 10 17
```

### 예제 출력 1

```text
15
```

### 예제 입력 2

```text
5 20
4 42 40 26 46
```

### 예제 출력 2

```text
36
```

## 시도

### 시도1

시간 제한은 1초이고, M의 사이즈가 최대 2 * (10 ** 9) 이라서 안 될 것 같았지만,
일단 구현하여 제출해보았으나 시간 초과로 실패했다.

단순히 뺄셈을 하여 구현하는 것이 아니라, 
알고리즘 분류의 힌트에서 알려주는 것 처럼 이분 탐색 또는 매개 변수 탐색을 이용하여 풀어야 할 것 같다.

```python
# https://www.acmicpc.net/problem/2805
# 나무 자르기
import sys

input = sys.stdin.readline

# N, M = map(int, input().split())  # N: 나무의 수, M: 나무의 길이
# trees = list(map(int, input().split()))
# N, M = 4, 7
# trees = [20, 15, 10, 17]
N, M = 5, 20
trees = [4, 42, 40, 26, 46]

answer = float("INF")

max_height = max(trees)
for i in range(max_height, -1, -1):
    current_result = 0
    for tree in trees:
        if tree - i > 0:
            current_result += tree - i

    if M == current_result and current_result <= answer:
        answer = i

print(answer)
```

### 시도2

binary search code는 오랜만에 구현해보는 거라 [위키 독스](https://wikidocs.net/233716)의 binary search 코드를 참고하여
이분 탐색 코드를 작성하여 문제를 풀어봤으나, 2%에서 시간 초과로 오답 처리 되었다.

```python
# https://www.acmicpc.net/problem/2805
# 나무 자르기
import sys

input = sys.stdin.readline


def binary_search(target, tree_list):
    start = 0
    end = max(tree_list)

    while start <= end:
        mid = (start + end) // 2

        result = 0
        for t in tree_list:
            if t > mid:
                result += t - mid

        if result == target:
            return mid
        elif result > target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


N, M = map(int, input().split())  # N: 나무의 수, M: 나무의 길이
trees = list(map(int, input().split()))
# N, M = 4, 7
# trees = [20, 15, 10, 17]
# N, M = 5, 20
# trees = [4, 42, 40, 26, 46]

answer = float("INF")

max_height = max(trees)
for i in range(max_height, -1, -1):
    current_result = 0
    for tree in trees:
        if tree - i > 0:
            current_result += tree - i

    if M == current_result and current_result <= answer:
        answer = i

print(binary_search(M, trees))
```

### 시도3

[블로그](https://dduniverse.tistory.com/entry/백준-이분탐색-나무-자르기-파이썬-python)를 참고하연 mid를 출력하는게 아닌, 
answer에 답을 계속해서 저장하여 값을 생성하는 것을 선택하였다.

하지만, 시간 초과로 오답 처리됨 (+ `total > M`이 아닌 `total >= M`으로 해야함)

```python
import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # N: 나무의 수, M: 나무의 길이
trees = list(map(int, input().split()))

start, end = 0, max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for t in trees:
        if t > mid:
            total += t - mid

    if total > M:  # 더 적게 가져갈 수 있다면
        start = mid + 1
        answer = mid  # 일단 최솟값을 저장
    else:  # 기준 미달이라면 ? end 를 앞으로 당겨서 더 작은 수를 minus
        end = mid - 1

print(answer)
```

### 시도4

시간 초과인 부분을 없애기 위해서 `if total >= M: break` 을 추가하여 이미 조건이 충족하면 break를 해주었다.

결과는 정답

```python
# https://www.acmicpc.net/problem/2805
# 나무 자르기

import sys

input = sys.stdin.readline

N, M = map(int, input().split())  # N: 나무의 수, M: 나무의 길이
trees = list(map(int, input().split()))
# N, M = 4, 7
# trees = [20, 15, 10, 17]
# N, M = 5, 20
# trees = [4, 42, 40, 26, 46]

start, end = 0, max(trees)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0

    for t in trees:
        if t > mid:
            total += t - mid
        if total >= M:
            break

    if total >= M:  # 더 적게 가져갈 수 있다면
        start = mid + 1
        answer = mid  # 일단 최솟값을 저장
    else:  # 기준 미달이라면 ? end 를 앞으로 당겨서 더 작은 수를 minus
        end = mid - 1

print(answer)

```

## 정리

