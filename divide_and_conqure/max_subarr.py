def find_max_crossing_subarr(arr, low, mid, high):
    left_sum = -float('inf')
    left_max = None
    s = 0
    
    for i in range(mid, low-1, -1):
        s += arr[i]
        
        if s > left_sum:
            left_sum = s
            left_max = i
    
    right_sum = -float('inf')
    right_max = None
    s = 0
    
    for i in range(mid+1, high+1):
        s += arr[i]
        
        if s > right_sum:
            right_sum = s
            right_max = i
    
    return (left_max, right_max, left_sum + right_sum)

def max_sub_arr(arr, low, high):
    if high == low:
        return (low, high, arr[low])
    
    mid = (low + high) // 2
    
    left_i, left_j, left_sum = max_sub_arr(arr, low, mid)
    right_i, right_j, right_sum = max_sub_arr(arr, low, mid)
    
    cross_i, cross_j, cross_sum = find_max_crossing_subarr(arr, low, mid, high)
    
    if left_sum > right_sum and left_sum > cross_sum:
        return (left_i, left_j, left_sum)
    elif right_sum > left_sum and right_sum > cross_sum:
        return (right_i, right_j, right_sum)
    else:
        return (cross_i, cross_j, cross_sum)


def max_sub_arr_linear(arr):
    max_sum = -float('inf')
    low = high = 0
    s = 0
    
    for i in range(len(arr)):
        if s <= 0:
            low = i
            s = arr[i]
        else:
            s += arr[i]
        
        if s > max_sum:
            max_sum = s
            low = i
            high = i + 1
    
    return low, high, max_sum    

arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(max_sub_arr(arr, 0, len(arr)-1))
print(max_sub_arr_linear(arr))