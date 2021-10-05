# write your python code below
import heapq
from collections import defaultdict

num_cities, num_roads = map(int, input().split())

G = defaultdict(list)

for _ in range(num_roads):
	from_c, to_c = map(int, input().split())	
	G[from_c].append(to_c)


print(G)

companey = int(input())

heap = [(0, companey)]
result = []
visited = {companey}

while len(heap) > 0:
	dist, cur = heapq.heappop(heap)
	for child in G[cur]:
		if child not in visited:
			heapq.heappush(heap, (dist+1, child))
			visited.add(child)
	
	if cur != companey:
		result.append(cur)

for i in result:
	print(i)
