class Node:
    def __init__(self, val, prev=''):
        self.val = val
        self.prev = prev
    
    def __eq__(self, o):
        return self.val == o.val
    
    def __hash__(self):
        return hash(f'{self.val}')
    
    def __str__(self):
        return f'{self.val}{self.prev}'
    
    def getPath(self):
        return f'{self}'[::-1]

def findNode(start, goal, G):
    stack = []
    stack.append(Node(start))
    
    visited = set()
    visited.add(Node(start))
    
    while len(stack) > 0:
        cur = stack.pop()
        
        if cur.val == goal:
            return cur
        
        for neighbor in G[cur.val]:
            node = Node(neighbor, cur)
            if node not in visited:
                stack.append(node)
                visited.add(node)
    
    return None
    

G = {
    1: [2, 3],
    2: [1],
    3: [1,4,5,6],
    4: [3],
    5: [3],
    6: [3,7,8],
    7: [6,8],
    8: [6,9,7],
    9: [8],
    10:[]
}

path = findNode(5,7, G)
print(path)

path = findNode(5,4, G)
print(path)

path = findNode(9,1, G)
print(path)

path = findNode(10,1, G)
print(path)