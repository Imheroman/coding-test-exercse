from collections import deque

# 리스트 생성
# my_list = [1, 2, 3, 4, 5]

# 리스트를 deque로 변환
my_deque = deque(list(map(int, input().split())))

# deque 내용 출력
print(my_deque)  # deque([1, 2, 3, 4, 5])
