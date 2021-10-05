nums = [1,1,1,1,1]
target = 3

stack = [[0,0]]

visited = {(0,0)}

count = 0

while len(stack) > 0:
    
    cur, idx = stack.pop()
    
    if cur == target:
        count += 1
    
    s = cur + nums[idx]
    if idx+1 < len(nums) and (s, idx+1) not in visited:
        stack.append((s,idx+1))
        visited.add((s,idx+1))
    
    s = cur - nums[idx]    
    if idx+1 < len(nums) and (s, idx+1) not in visited:
        stack.append((s,idx+1))
        visited.add((s,idx+1))
        
        

print(count)
