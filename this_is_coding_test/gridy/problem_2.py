n, m, k = map(int, input().split())
# n, m, k = 5, 7, 2

number_list = list(number for number in range(n))
# number_list = [2, 4, 5, 4, 6]
# number_list = [3, 4, 3, 4, 3]
number_list.sort()
max_number = number_list[-1]
max_number_2 = number_list[-2]

count = (m // (k + 1)) * k

result = max_number * count + max_number_2 * (m-count)
print(result)
