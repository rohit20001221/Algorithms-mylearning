def dfs(start, G, stack, visited):
    visited[start] = True

    for neighbor in G[start]:
        if not visited[neighbor]:
            dfs(neighbor, G, stack, visited)

    stack.append(start)
    return


def topological(G):
    stack = []
    visited = {i: False for i in G}

    for i in G:
        if not visited[i]:
            dfs(i, G, stack, visited)

    while len(stack) > 0:
        print(stack.pop(), end=" ")


G = {"0": ["2", "3"], "1": [], "2": [], "3": ["1"], "4": ["2", "1"], "5": ["2", "0"]}

print(topological(G))
