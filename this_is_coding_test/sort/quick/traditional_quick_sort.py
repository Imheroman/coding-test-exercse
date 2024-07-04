# def partition(arr, start, end):
#     pivot = arr[start]
#     left = start + 1
#     right = end
#
#     while left <= right:
#         while arr[left] < pivot:
#             left += 1
#         while arr[right] > pivot:
#             right -= 1
#
#         if left <= right:
#             arr[left], arr[right] = arr[right], arr[left]
#     return right
#
#
# def quick_sort(arr, start, end):
#     if start >= end:
#         return
#
#     pivot = partition(arr, start, end)
#     quick_sort(arr, start, pivot - 1)
#     quick_sort(arr, pivot + 1, end)
#
#
# number_list = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# quick_sort(number_list,0, len(number_list)-1)
# print(number_list)
