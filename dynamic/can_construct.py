def canConstruct(target : str, wordBank, m):
    if(target == ''):
        return 1
    
    total_count = 0
    # remove all the prefixes from the word bank
    for word in wordBank:
        try:
            index = target.index(word)
        except:
            index = -1
        if index == 0:
            suffix = target[len(word):]
            if suffix not in m:
                m[suffix] = canConstruct(suffix, wordBank, m)
            
            total_count += m[suffix]
        
    return total_count

m = {}
print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd'], m))
m = {}
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeee', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
], m))