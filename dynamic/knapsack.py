class Item:
    def __init__(self, weight, profit):
        self.weight = weight
        self.profit = profit


items = [
    Item(3, 6), Item(2, 8), Item(4, 7)
]


max_weight = 8

print(f"Total possibilities: {2**len(items)}")

def solve(items, max_weight, m={}):
    # return knapsack_01(items, max_weight, len(items) - 1, m={})
    return knapsack_01(items, max_weight, len(items)-1, m)

def knapsack_01(items, space, index, m):
    
    if space <= 0 or index <= 0:
        return 0
    
    # find the key
    key = f"{index}{space}"
    
    if key in m:
        return m[key]
    else:
        # profit when including an item
        inc = items[index].profit + knapsack_01(items, space - items[index].weight, index - 1, m)
        # profit when excluding an item
        exc = knapsack_01(items, space, index - 1, m)
        m[key] = max(inc, exc)
    
    
    # return max profit
    return m[key]

def knapsack_01_tabluation(items, space):    
    table = [[0]*(space)]*(len(items))
    
    for i in range(len(items)):
        for j in range(space):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif items[i].weight <= j:
                table[i][j] = max(table[i-1][j], table[i-1][j - items[i].weight] + items[i].profit)
    
    return table

print(solve(items, max_weight))