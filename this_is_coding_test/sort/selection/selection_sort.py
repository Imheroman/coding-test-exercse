number_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(number_list)):
    min_index = i
    print("="*50)

    for j in range(i + 1, len(number_list)):
        if number_list[min_index] > number_list[j]:
            min_index = j

    number_list[min_index], number_list[i] = number_list[i], number_list[min_index]

print(number_list)
