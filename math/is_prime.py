import datetime

# this is the fastest algorithm
def isPrime(n):
    count = 0
    i = 2
    
    while i*i <= n:
        if n % i == 0:
            count += 1
            break
        i += 1
    
    return count == 0


def steveAlgo(n):
    # generate all numbers from 1 to n
    data = list(range(2, n+1))
    map_ = [True] * (n-1)
    
    for i in range(len(data)):
        if map_[i] == True:
            for j in range(i, len(data)):
                if data[j] != data[i] and data[j] % data[i] == 0:
                    map_[j] = False
    
    result = []
    
    for i in range(len(data)):
        if map_[i] == True:
            result.append(data[i])

    return result

'''
t1 = datetime.datetime.now()
print(steveAlgo(10000))
t2 = datetime.datetime.now()

print(t2 - t1, end="\n")

for i in range(10000):
    if isPrime(i):
        print(i, end=" ")
'''
#t3 = datetime.datetime.now()

#print(t3 - t2, end="\n")

# for i in reversed(range(10**10)):
# 	#if isPrime(i):
# 	#	print(i)
# 	print(i)
