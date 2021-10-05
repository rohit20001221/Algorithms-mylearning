from disjointset import Unionfind

n = int(input()) # number of nodes
e = int(input()) # number of edges

spanning_tree = Unionfind(n)

edges = []

for _ in range(e):
    a, b, weight = list(map(int, input().split()))
    edges.append((a, b, weight))
    # edges.append((b, a, weight))

edges.sort(key=lambda x : x[2])
print(edges)
edges_ = []

for edge in edges:
    u, v, weight = edge
    
    if spanning_tree.find(u) == spanning_tree.find(v):
        continue
    else:
        spanning_tree.union(u, v)
        edges_.append((u, v))
    
print(edges_)