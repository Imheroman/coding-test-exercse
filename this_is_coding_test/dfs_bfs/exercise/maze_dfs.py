def maze_dfs(maze, pos, directions, n, m):
    from collections import deque
    visited = []
    need_to_visit = deque()
    need_to_visit.append(pos)

    while need_to_visit:
        px, py = need_to_visit.pop()

        for dx, dy in directions:
            x = px + dx
            y = py + dy

            if x < 0 or x >= n or y < 0 or y >= m:
                continue

            if maze[x][y] == 1 and (x, y) not in visited:
                visited.append((x, y))
                need_to_visit.append((x, y))
                maze[x][y] = maze[px][py] + 1

    return maze[n-1][m-1]


n, m = 5, 6
graph = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
counting = maze_dfs(graph, (0, 0), directions, n, m)
print("count:", counting)
