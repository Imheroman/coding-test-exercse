from collections import deque


def bfs(graph, row, visited):
    queue = deque([row])
    visited[row] = True

    while queue:
        pop_value = queue.popleft()
        print(pop_value, end=" ")

        for number in graph[pop_value]:
            if not visited[number]:
                queue.append(number)
                visited[number] = True


visited = [False] * 9
visitor = 1
GRAPH = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

bfs(GRAPH, visitor, visited)


