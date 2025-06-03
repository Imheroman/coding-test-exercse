# [24060번: 병합 정렬](https://www.acmicpc.net/problem/24060)

오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A에 K 번째 저장되는 수를 구해서 우리 서준이를 도와주자.

크기가 N인 배열에 대한 병합 정렬 의사 코드는 다음과 같다.

```text
merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
    if (p < r) then {
        q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
        merge_sort(A, p, q);      # 전반부 정렬
        merge_sort(A, q + 1, r);  # 후반부 정렬
        merge(A, p, q, r);        # 병합
    }
}

# A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
merge(A[], p, q, r) {
    i <- p; j <- q + 1; t <- 1;
    while (i ≤ q and j ≤ r) {
        if (A[i] ≤ A[j])
        then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
        else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
    }
    while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
        tmp[t++] <- A[i++];
    while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
        tmp[t++] <- A[j++];
    i <- p; t <- 1;
    while (i ≤ r)  # 결과를 A[p..r]에 저장
        A[i++] <- tmp[t++]; 
}
```

## 입출력

### 입력
첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 저장 횟수 K(1 ≤ K ≤ 108)가 주어진다.

다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

### 출력
배열 A에 K 번째 저장 되는 수를 출력한다. 저장 횟수가 K 보다 작으면 -1을 출력한다.

## 예제

### 예제 입력 1

```text
5 7
4 5 1 3 2
```

### 예제 출력 1

```text
3
```
4 5 1 3 2 -> **4** 5 1 3 2 -> 4 **5** 1 3 2 -> **1** 5 1 3 2 -> 1 **4** 1 3 2 -> 1 4 **5** 3 2 -> 1 4 5 **2** 2 -> 1 4 5 2 **3** -> **1** 4 5 2 3 -> 1 **2** 5 2 3 -> 1 2 **3** 2 3 -> 1 2 3 **4** 3 -> 1 2 3 4 **5**. 
총 12회 저장이 발생하고 일곱 번째 저장되는 수는 3이다.
### 예제 입력 2

```text
5 13
4 5 1 3 2
```

### 예제 출력 2

```text
-1
```

## 알고리즘 분류

- 구현
- 정렬
- 재귀

## 시도

### 시도1(오답)

병합 정렬을 구현하여 K번째에 저장되는 수를 출력하는 문제이다.

솔직히 병합 정렬을 의사 코드 보고 구현하는 것은 어렵지 않았지만, K번째 저장된다는게 무슨 뜻인지 이해가 잘 안 돼서 다른 블로그를 참고했다.

[Interrobang](https://interrobang.tistory.com/90)님의 블로그를 보고 참고한 결과
저장된 결과를 기존 배열에 복사할 때 마다 `count`를 하면 된다고 이해했다.

나는 의사 코드를 보고 작성한 코드보다 `list slicing`을 이용한 코드가 더 깔끔하고 보기 좋다고 생각해 아래와 같이 작성했는데,
오답이 나왔다 ,,,!

```python
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    merge_result = merge(left, right)
    return merge_result


def merge(left, right):
    result = []
    l = r = 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1

    global count
    for res in result:
        count += 1
        if count == K:
            print(res)
            exit()

    return result


count = 0
merge_sort(A)
print(-1)
```

### 시도2

의사 코드대로 작성하고 통과

```python
import sys

input = sys.stdin.readline

# N, K = map(int, input().split())
# A = list(map(int, input().split()))
N, K = 5, 7
A = [4, 5, 1, 3, 2]


def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    result = []
    s, e = start, mid + 1

    while s <= mid and e <= end:
        if arr[s] <= arr[e]:
            result.append(arr[s])
            s += 1
        else:
            result.append(arr[e])
            e += 1

    while s <= mid:
        result.append(arr[s])
        s += 1

    while e <= end:
        result.append(arr[e])
        e += 1

    s = start
    t = 0

    global count
    while s <= end:
        arr[s] = result[t]
        count += 1

        if count == K:
            print(arr[s])
            exit()

        s, t = s + 1, t + 1


count = 0
merge_sort(A, 0, len(A) - 1)
print(-1)
```
