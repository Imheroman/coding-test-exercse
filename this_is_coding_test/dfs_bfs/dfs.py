def dfs(graph, visitor, visited):
    print(visitor, end=" ")
    visited[visitor] = True

    for neighbor in graph[visitor]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


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

dfs(GRAPH, visitor, visited)

