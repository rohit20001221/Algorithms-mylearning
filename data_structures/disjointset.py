class Unionfind:
    
    def __init__(self, n):
        self.graph = {}
        
        for i in range(n):
            self.graph[i] = -1
    
    def find(self, s):
        # iterative method for finding the root element
        if s in self.graph:
            root = s
            if self.graph[root] == -1:
                return root
            
            while self.graph[root] != -1:
                root = self.graph[root]
            
            return root
        
        return None
    
    def union(self, u, v):
        a = self.find(u)
        b = self.find(v)
        if a == b:
            return
        self.graph[a] = b
        return
    
    def __repr__(self):
        return f"{self.graph}"
            
if __name__ == '__main__':
    n = 7
    union = Unionfind(n)
    print(union)

    arr = [[0,1], [1,2], [2,3], [4,5]]

    for u, v in arr:
        union.union(u,v)

    print(union)
    print(union.find(1))
    print(union.find(3))
    print(union.find(4))
    print(union.find(6))