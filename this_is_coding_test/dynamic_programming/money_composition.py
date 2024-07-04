# n, m = map(int, input().split())
# money_list = list(int(input()) for _ in range(n))
# n, m = 2, 15
# money_list = [2, 3]
# memorization = [0] * (m + 1)
#
# for i in range(1, m + 1):
#     print(f"{i}: {memorization}")
#     for money in money_list:
#         if i % money == 0:
#             memorization[i] = min(memorization[i - 1], memorization[i // money] + 1)
#         else:
#             memorization[i] = memorization[i] + 1
#
# print(memorization)
