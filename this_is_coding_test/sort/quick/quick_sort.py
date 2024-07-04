def quick_sort(start, end, arr):
    if start >= end:  # 탐색 시작이 end이거나 end보다 크면 종료
        return

    pivot = start  # 첫 원소
    left = start + 1  # pivot 다음 원소
    right = end  # 마지막 원소

    # left와 right가 계속 초기화 되는 것이 아님
    while left <= right:  # 왼쪽의 범위가 오른쪽 범위를 넘을 때 까지 --> pivot을 기준으로 큰 수와 작은 수를 정렬이 끝날 때 까지
        while left <= end and arr[pivot] > arr[left]:  # pivot보다 큰 수를 찾기 위해 계속해서 오른쪽으로 이동
            left += 1
        while start <= right and arr[pivot] < arr[right]:  # pivot보다 작은 수를 찾기 위해 계속해서 왼쪽으로 이동
            right -= 1

        if left > right:  # 만약 왼쪽 범위가 오른쪽 범위를 넘으면
            arr[right], arr[pivot] = arr[pivot], arr[right]  # pivot과 오른쪽 범위의 number을 변경
        else:  # 정상이라면
            arr[left], arr[right] = arr[right], arr[left]  # 큰 수와 작은 수를 변경

    quick_sort(start, right - 1, arr)  # quick 정렬의 오른쪽(마지막 탐색을 마친 인덱스?)을 끝으로 설정하고 재탐색
    quick_sort(right + 1, end, arr)  # quick 정렬의 오른쪽(마지막 탐색을 마친 인덱스?)을 시작으로 설정하고 재탐색


# data
number_list = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(0, len(number_list) - 1, number_list)
print(number_list)
