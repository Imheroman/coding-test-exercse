def quick_sort(arr):
    print("in quick arr:", arr)
    if len(arr) <= 1:
        return arr

    pivot = arr[0]  # 가장 왼쪽의 수를 pivot 설정
    tail = arr[1:]  # pivot을 제외한 나머지 numbers

    left = [x for x in tail if x <= pivot]  # pivot보다 작은 number들을 모두 저장
    right = [x for x in tail if x > pivot]  # pivot보다 큰 number들을 모두 저장

    return quick_sort(left) + [pivot] + quick_sort(right)  # 재귀적으로 왼쪽으로 계속 파고든 후 오른쪽 탐방
    # return quick_sort(right) + [pivot] + quick_sort(left)  # 내림차순으로 하고 싶으면


number_list = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort(number_list))
