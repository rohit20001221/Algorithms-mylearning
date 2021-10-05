def gridTraveller(m,n):
    table = [[0]*(n+1)]*(m+1)
    table[1][1] = 1
    
    for i in range(1,len(table)):
        for j in range(1, len(table[0])):
            
            table[i][j] = table[i-1][j] + table[i][j-1]
    
    return table[m][n]

print(gridTraveller(3,3))