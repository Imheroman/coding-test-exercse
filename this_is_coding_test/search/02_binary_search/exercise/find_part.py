def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid - 1
        elif array[mid] < target:
            start = mid+1
        else:
            return mid

    return -1


n = 5  # n = int(input())  # 5
stock = sorted([8, 3, 7, 9, 2])  # stock = sorted(map(int, input().split()))  # 8 3 7 9 2
m = 3  # m = int(input())  # 3
part_list = [5, 7, 9]  # part_list = list(map(int, input().split()))  # 5 7 9

for part in part_list:
    result = "yes" if binary_search(stock, part, 0, len(stock) - 1) != -1 else "no"
    print(result, end=" ")

