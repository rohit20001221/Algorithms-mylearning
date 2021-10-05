n = input()
arr = list(map(int, input().split()))

points = []

while len(arr) > 0:
    points.append([arr.pop(0), arr.pop(0)])

initialSlope = None
isLine = True

for i in range(1,len(points)):
    prev = points[i-1]
    cur = points[i]
    
    slope = (cur[1]-prev[1])/(cur[0]-prev[0])
    
    if initialSlope == None:
        initialSlope = slope
    else:
        if initialSlope  != slope:
            isLine = False
            break

if isLine:
    a = points[0]
    b = points[1]
    
    c1 = (b[1]-a[1])
    c2 = (b[0]-a[0])
    
    equation = f'{c1}x - {c2}y = 0'
else:
    equation = '0'

print(equation)