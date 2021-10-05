import heapq

def dijkastras(G, source):
    # declare a priority queue
    q = []
    dist = {}
    prev = {}
    
    dist[source] = 0
    prev[source] = -1
    
    for vertex in G:
        if vertex != source:
            dist[vertex] = float('inf')
            prev[vertex] = None

        heapq.heappush(q, [dist[vertex], vertex])
    
    # print("dist ", dist)
    # print("prev ", prev)
    
    while len(q) > 0:
        d, vertex = heapq.heappop(q)
        
        for neighbor in G[vertex]:
            alt = d + neighbor[1]
            # print("neighbor ",neighbor)
            # print("alt ",alt)
            if alt < dist[neighbor[0]]:
                dist[neighbor[0]] = alt
                prev[neighbor[0]] = vertex
                
                # decrease the priority of neighbour to v
                for i in range(len(q)):
                    if q[i][1] == neighbor[0]:
                        q[i][0] = alt
                        break
                
                heapq.heapify(q)
    
    return dist, prev                        
    
G = {
    1:[(2,2),(3,4)],
    2:[(4,7),(3,1)],
    3:[(5,3)],
    4:[(6,1)],
    5:[(4,2),(6,5)],
    6:[]
}

print(dijkastras(G, 1))