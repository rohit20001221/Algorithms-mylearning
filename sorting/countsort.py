arr = [1, 4, 1, 2, 7, 5, 2]

max_element = max(arr)

temp = [0] * (max_element + 1)

result = [0] * (len(arr))

for i in arr:
    temp[i] += 1

for i in range(1, len(temp)):
    temp[i] += temp[i - 1]

print(temp)

for i in arr:
    index = temp[i]
    result[index - 1] = i
    temp[i] -= 1

print(result)
