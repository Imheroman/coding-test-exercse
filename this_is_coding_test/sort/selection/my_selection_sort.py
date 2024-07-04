def print_numbers(numbers):
    for number in numbers:
        print(f"{number:2}", end="")
    print()
    print("=" * 50)


number_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
end = len(number_list)

for start in range(end):
    min_index = start

    for index in range(start, end):
        if number_list[min_index] > number_list[index]:
            min_index = index

    number_list[start], number_list[min_index] = number_list[min_index], number_list[start]
    print("changed number:", number_list[min_index], "and", number_list[start])
    print_numbers(number_list)




