def maxConZeros(arr):
    count = 0
    max_count = 0
    last_index = None
    start_index = None
    flag = True
    
    for i in range(len(arr)):
        if arr[i] == 0:
            count += 1
            
            if count > max_count:
                max_count = count
                last_index = i
                  
            if flag:
                start_index = i
                flag = False
        else:
            count = 0
            flag = True
    
    return max_count, start_index, last_index

T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    count, first, last = maxConZeros(A)

    while Y > 0:

        if Y > 0 and (first - 1) >= 0:
            A[first-1] = 0
            Y -= 1
            first -= 1
            count += 1
        
        if Y > 0 and (last + 1) < len(A):
            A[last+1] = 0
            Y -= 1
            last += 1
            count += 1
    
    while X > 0:
        
        if X > 0 and (first - 1) >= 0:
            A[first-1] -= 1
            X -= 1
            first -= 1

            if A[first] == 0:
                count += 1
        
        if X > 0 and (last + 1) < len(A):
            A[last+1] -= 1
            X -= 1
            last += 1

            if A[last] == 0:
                count += 1
       
        
    print(count)