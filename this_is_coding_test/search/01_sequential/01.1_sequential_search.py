# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:  # find target
            return i + 1  # return index

    return -1


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자를 입력하시요.")
n, target = input().split()
'''
5 Hero
'''

print("적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()
'''
Hanul Jonggu Hero Taeil Sangwook
'''

index = sequential_search(int(n), target, array)
if index == -1:
    print("존재하지 않습니다.")
else:
    print(f"해당 문자열은 {index}에 있습니다.")
