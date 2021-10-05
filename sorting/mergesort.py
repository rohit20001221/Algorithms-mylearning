def merge_sort(arr):
    
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
        
    return merge(left, right)

def merge(left, right):
    i, j = 0, 0
    result = []
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

print(merge_sort([1,10,9,3,2,6,4,5]))