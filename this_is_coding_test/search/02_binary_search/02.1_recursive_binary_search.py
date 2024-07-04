def recursive_binary_search(array, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if array[mid] == target:
        return mid + 1
    elif array[mid] > target:
        return recursive_binary_search(array, target, start, mid - 1)
    else:
        return recursive_binary_search(array, target, mid + 1, end)


target = int(input("찾고자 하는 원소를 입력하시오: "))
# 7
array = list(map(int, input("전체 원소를 입력하시오: ").split()))
# 1 3 5 7 9 11 13 15 17 19

index = recursive_binary_search(array, target, 0, len(array) - 1)
if index == -1:
    print("원소가 존재하지 않습니다.")
else:
    print(f"원소가 {index}에 존재합니다.")
