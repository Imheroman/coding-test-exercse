def recursive_maze_dfs(maze, pos, directions, n, m, visited=[]):
    visited.append(pos)
    px, py = pos

    for dx, dy in directions:
        x = px + dx
        y = py + dy

        if x < 0 or x >= n or y < 0 or y >= m:
            continue

        if maze[x][y] == 1 and (x, y) not in visited:
            maze[x][y] = maze[px][py] + 1
            recursive_maze_dfs(maze, (x, y), directions, n, m)


n, m = 5, 6
graph = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1]
]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우
recursive_maze_dfs(graph, (0, 0), directions, n, m)
goal = graph[n - 1][m - 1]
print(goal)
