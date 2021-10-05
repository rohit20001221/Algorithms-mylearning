INF = float('inf')

A = [
    [(0,None), (3,None),   (INF,None), (7,None)],
    [(8,None), (0,None),   (2,None),   (INF,None)],
    [(5,None), (INF,None), (0,None),   (1,None)],
    [(2,None), (INF,None), (INF,None), (0,None)]
]

for k in range(len(A)):
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] = min(A[i][j], (A[i][k][0] + A[k][j][0], k), key=lambda x : x[0])
            
for row in A:
    print(row)

source = 2
target = 0

search = A[source][target]
paths = [source]

# print(search)

while search[1] != None:
    # print(search)
    paths.append(search[1])
    search = A[search[1]][target]

paths.append(target)
print(paths)
