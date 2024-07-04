def my_sequential_search(target, array):
    for index in range(len(array)):
        print("array[index]:", array[index])
        print("target:", target)
        if array[index] == target:
            return index + 1
    return -1


print("찾을 문자를 입력하시요.")
target = input()
'''
Hero
'''

print("문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()
'''
Hanul Jonggu Hero Taeil Sangwook
'''

index = my_sequential_search(target, array)
if index == -1:
    print("존재하지 않습니다.")
else:
    print(f"해당 문자열은 {index}에 있습니다.")