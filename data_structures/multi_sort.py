# write your python code below

def merge_sort(arr):
	if len(arr) <= 1:
		return arr
	
	low = 0
	high = len(arr)
	
	mid = (low + high) // 2
	
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	
	return merge(left, right)

def merge(left, right):
	i, j = 0, 0
	result = []
	
	while i < len(left) and j < len(right):
		if left[i][1] > right[j][1]:
			result.append(left[i])
			i += 1
		elif left[i][1] < right[j][1]:
			result.append(right[j])
			j += 1
		else:
			if left[i][0] > right[j][0]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
	
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1
	
	return result


if __name__ == '__main__':
	print(merge_sort([(1, 2), (2, 2), (6, 1)]))
