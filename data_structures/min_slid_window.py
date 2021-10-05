import heapq

arr = [1,3,-1,-3,5]

maxheap = []
result = []

n, k = 5, 3

# built a min heap for n elements
for i in range(k):
    heapq.heappush(maxheap, (-arr[i], i))

result.append(-maxheap[0][0])

for cur in range(k,n):
    max_, idx_max = maxheap[0]
    
    while idx_max <= cur - k:
        heapq.heappop(maxheap)
            
    heapq.heappush(maxheap, (-arr[cur], cur))
    result.append(-maxheap[0][0])
    
print(result)