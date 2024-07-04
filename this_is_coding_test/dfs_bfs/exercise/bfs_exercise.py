from collections import deque

# n, m = map(int, input().split())
# graph = [list(map(int, input())) for _ in range(n)]
"""
101010
111111
000001
111111
111111
"""
n, m = 5, 6
graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 x == row / y == column


def print_maze(maze):
    for row in maze:
        for number in row:
            print(f"{number:3}", end="")
        print()
    print("=" * 50)


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # x, y 좌표를 set으로 queue에 저장

    while queue:  # queue가 빌 때 까지
        print_maze(graph)
        x, y = queue.popleft()  # 처음 삽입한 데이터를 꺼냄
        for direction_x, direction_y in direction:  # 모든 방향을 탐색
            nx = x + direction_x  # x에 탐색할 방향을 더함
            ny = y + direction_y  # y에 탐색할 방향을 더함

            if nx < 0 or ny < 0 or nx >= n or ny >= m:  # 경계선을 넘어갔을 때
                continue

            if graph[nx][ny] == 0:  # 막다른 길(벽) 일때
                continue

            if graph[nx][ny] == 1:  # 처음 방문하는 노드일 경우
                graph[nx][ny] = graph[x][y] + 1  # 다음 길을 +1
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))
