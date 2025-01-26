from operator import attrgetter

class Item:
    def __init__(self, item_weight: int, item_value: int):
        self.weight = item_weight
        self.value = item_value
    
    
class Knapsack:
    def __init__(self, weight: int, items):
        self.max_weight = weight
        self.item_list = items        