number_list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(number_list)):
    for j in range(i, 0, -1):
        if number_list[j] < number_list[j - 1]:
            number_list[j], number_list[j - 1] = number_list[j - 1], number_list[j]

        else:
            break

print(number_list)


