def insertion_sort(numbers):
    for i in range(1, len(numbers)):  # i == 선택된 index
        for j in range(i, 0, -1):  # 삽입할 위치를 찾음
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
        print(numbers)


number_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
insertion_sort(number_list)
print(number_list)
