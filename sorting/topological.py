from collections import defaultdict


def DFS(G, root, visited, stack):
    visited.add(root)

    for neighbor in G[root]:
        if neighbor not in visited:
            DFS(G, neighbor, visited, stack)

    stack.append(root)


def topological_sort(G):
    visited = set()
    stack = []

    for root in G:
        if root not in visited:
            DFS(G, root, visited, stack)

    return stack


G = defaultdict(list)

n = int(input())

for _ in range(n):
    u, v = input().split()
    G[u].append(v)

    G[v] = []

print(topological_sort(G))
