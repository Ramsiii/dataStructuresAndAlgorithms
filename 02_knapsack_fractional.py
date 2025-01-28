# An individual item with a weight and value
# fraction starts out as a whole 
class Item:
    def __init__(self, item_weight, item_value, item_name):
        self.weight = item_weight
        self.value = item_value
        self.fraction = 1.0
        self.name = item_name

# The knapsack that contains a list of items and a maximum
# total weight
class Knapsack:
    def __init__(self, max_weight, items):
        self.max_weight = max_weight
        self.item_list = items

# A function used to calculate the value to weight ratio
def value_to_weight_ratio(item):
    return item.value / item.weight

# The Fractional Knapsack algorithm - knapsack is an instance of the Knapsack Class
def fractional_knapsack(knapsack, item_list):
    # Sort the items in descending order based on value/weight
    item_list.sort(key = value_to_weight_ratio, reverse = True)

    remaining = knapsack.max_weight
    for item in item_list:
        # Check if the full item can fit into the knapsack or
        # only a fraction
        if item.weight <= remaining and remaining > 0:
            # The full item will fit. 
            knapsack.item_list.append(item)
            remaining -= item.weight

        elif item.weight >= remaining and remaining > 0:
            # Only a fractional part of the item will fit. Add that
            # fraction of the item, and then exit.
            item.fraction = remaining / item.weight
            knapsack.item_list.append(item)
            remaining -= item.fraction  
            break
        
        
if __name__ == '__main__':
    
    item1 = Item(5, 7, 'tofu')
    item2 = Item(18, 10, 'rice')
    item3 = Item(12, 13, 'beans')
    item4 = Item(4, 8, 'apples')
    item5 = Item(10, 8, 'bananas')
    item6 = Item(2, 1, 'tomato')
    
    item_list = [item1, item2, item3, item4, item5, item6]
    
    # initialize knapsack with an empty list
    knapsack = Knapsack(30, [])
    
    # add items to the knapsack one at a time and then 
    # only a fraction of the last item
    fractional_knapsack(knapsack, item_list)
    
    total_weight = 0
    total_value = 0
    
    print('\nItems in knapsack:')
    print('\nName\t\tWeight\tValue\tFraction')
    print('-' * 50)
    
    for item in knapsack.item_list:
        
        actual_weight = item.weight * item.fraction
        actual_value = item.value * item.fraction
        
        total_weight += actual_weight
        total_value += actual_value
        
        
        print(f'{item.name}\t\t{item.weight}\t{item.value}\t{item.fraction:.2f}')
    
    print(f'\nThe total weight in the knapsack is: {total_weight}\nThe total value in the knapsack is: {total_value:.2f}')


    
    
    
    
    