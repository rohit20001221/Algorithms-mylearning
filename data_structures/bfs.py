from collections import deque


def BFS(G, root, target):

    visited = set()
    q = deque([])

    steps = 0

    visited.add(root)
    q.append(root)

    while len(q) > 0:

        steps += 1

        for _ in range(len(q)):
            cur = q.popleft()

            if cur == target:
                return steps

            for neighbor in G[cur]:

                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

    return -1
