class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit


items = [
    Item(3, 6), Item(2, 8), Item(4, 7), Item(2,8), Item(2, 8)
]


max_weight = 8

s = [[0,0, ""]]

for i in range(len(items)):
    # exclude the item
    s_0 = []
    
    for tup in s:
        tup_ = tup[:]
        tup_[2] += "0"
        s_0.append(tup_)
            
    # exclude the item
    s_1 = []
    
    for tup in s:
        items_ = tup[2][:]
        items_ += "1"
        t_ = [tup[0] + items[i].weight, tup[1] + items[i].profit, items_]
        if t_[0] <= max_weight:
            s_1.append(t_)
    
    s = s_0 + s_1

print(max(s, key=lambda x : x[1]))