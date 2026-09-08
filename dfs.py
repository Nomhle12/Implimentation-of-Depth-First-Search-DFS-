def dfs(graph,start):
    visited = []

    def visit(node):
        visited.append(node)

        for neighbor in range(len(graph)):
            if graph[node][neighbor] == 1 and neighbor not in visited:
                visit(neighbor)

    visit(start)
    return visited

print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 0]], 3))
print(dfs([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]], 0))
