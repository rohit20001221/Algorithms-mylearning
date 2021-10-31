def DFS(G, root, target):

    visited = set()
    stack = []

    visited.add(root)
    stack.append(root)

    while len(stack) > 0:

        cur = stack.pop()

        if cur == target:
            return True

        for neighbor in G[cur]:

            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False
