from collections import defaultdict

'''
sample test case
10
1 5
1 2
2 5
3 5
2 3
2 6
3 6
1 3
1 4
4 3
4
'''

n = int(input())
G = defaultdict(list)

for _ in range(n):
    a, b = input().split()
    G[a].append(b)
    G[b].append(a)

m = int(input())

def generate_candidates(G, current_node, color_map, m):
    colors = set(range(m))
    assigned = set()
    for node in G[current_node]:
        if color_map[node] != None:
            assigned.add(color_map[node])
    
    return colors - assigned


def back_track_helper(G, nodes, idx, color_map, m, results):
    # return the result if the index has reached to last
    if idx >= len(nodes):
        results.append(color_map)
        return
    
    for candidate in generate_candidates(G, nodes[idx], color_map, m):
        # assign the color to the
        color_map[nodes[idx]] = candidate
        back_track_helper(G, nodes, idx+1, color_map.copy(), m, results)
        color_map[nodes[idx]] = None
    
    

def back_tracK(G, nodes, m):
    results = []
    color_map = {}
    
    for i in nodes:
        color_map[i] = None
    
    back_track_helper(G, nodes, 0, color_map, m, results)
    return results

for result in back_tracK(G, list(G.keys()), m):
    print(result)