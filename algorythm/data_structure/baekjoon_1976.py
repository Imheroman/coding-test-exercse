# https://www.acmicpc.net/problem/1976
# 여행가자
# 거의 참고 안 한 참고 블로그 ,, : https://eunjng.tistory.com/85
from sys import stdin
input = stdin.readline


def find_root(p, x):
    if x != p[x]:
        p[x] = find_root(p, p[x])

    return p[x]


def union_root(p, c, y):
    x = find_root(p, c)
    y = find_root(p, y)
    # print("p:", p, "-> x:", x, ", y:", y)

    if x > y:
        p[x] = y
    else:
        p[y] = x


N = int(input())  # 도시 수
M = int(input())  # 방문 도시 수
cities = [index for index in range(N)]  # 유니온 파인드
for current_index in range(N):
    city_paths = list(map(int, input().rstrip().split()))
    for index, is_connected in enumerate(city_paths):
        if is_connected:  # 연결되어 있는 경우
            union_root(cities, current_index, index)  # 노드를 합침
plans = list(map(lambda x: int(x) - 1, input().split()))
answer = "YES"

for current_index in range(1, M):
    pre = plans[current_index - 1]  # 이전 방문 노드
    current = plans[current_index]  # 현재 방문 노드
    print("current:", current, ", pre:", pre)
    if cities[pre] != cities[current]:  # 이전 방문 노드와 현재 방문 노드가 다르다면 연결되어 있지 않은 것임
        answer = "NO"
        break

# print("cities:", cities)
print(answer)
