def quicksort(arr, l, h):
    if l < h:
        pivot = partition(arr, l, h)
        quicksort(arr, l, pivot)
        quicksort(arr, pivot + 1, h)


def partition(arr, l, h):
    pivot = (l+h) // 2
    
    i = l - 1
    j = h + 1
    
    while(1):
        i += 1
        while arr[i] < arr[pivot]:
            i += 1
        j -= 1
        while arr[j] > arr[pivot]:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]
        
arr = [1,10,9,3,2,6,4,5]
quicksort(arr, 0, len(arr) - 1)
print(arr)