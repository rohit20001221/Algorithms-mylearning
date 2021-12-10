def solution(A, K):
	
	birds = []
	count = 0
	
	for i in range(len(A)):
		for j in range(len(A[0])):
			
			# find the coordinates of the birds
			if A[i][j] == 1:
				birds.append((i, j))
	
	# iterate through whole array
	for i in range(len(A)):
		for j in range(len(A[0])):
			
			for ib, jb in birds:
				
				if abs(ib - i) + abs(jb - j) <= k:
					count += 1
	
	
	return count
