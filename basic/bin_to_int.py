def binToInt(s):
    num = 0
    
    for i in range(len(s)-1, -1, -1):
        num += int(s[i]) * (2**(len(s)-i-1))
    
    return num

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    s = input()
    s_ = s

    k = 1

    max_num = binToInt(s)

    while k < len(s):
        s_ = s_[1:] + s_[:1]
        n = binToInt(s_)
        if n > max_num:
            max_num = n
        k += 1
    
    t = 0

    while K > 0:
        s = s[1:] + s[:1]
        if binToInt(s) == max_num:
            K -= 1
        
        t += 1
    
    print(t)