from operator import attrgetter

class Item:
    def __init__(self, item_weight: int, item_value: int):
        self.weight = item_weight
        self.value = item_value
     
class Knapsack:
    def __init__(self, weight: int, items):
        self.max_weight = weight
        self.item_list = items        

def knapsack_01(knapsack, item_list):
    item_list.sort(key = attrgetter('value'), reverse = True)
    
    remaining = knapsack.max_weight
    for item in item_list:
        if item.weight <= remaining:
            knapsack.item_list.append(item)
            remaining = remaining - item.weight
    
# main program:

# instances of the Item class with (item_weight, item_value)
item_1 = Item(6, 25)
item_2 = Item(8, 42)
item_3 = Item(12, 60)
item_4 = Item(18, 95)

# above items stored in a list - item_list is the argument passed to the knapsack_01 function
item_list = [item_1, item_2, item_3, item_4]

# empty list to be passed as the second argument (items) of the knapsack instance of the Knapsack class 
initial_knapsack_list = []

# max_weight defined by user input
max_weight = int(input('Enter the maximum weight the knapsack can hold: '))

# instance of the Knapsack class storing max_weight and empty initial_knapsack_list from above
knapsack = Knapsack(max_weight, initial_knapsack_list)

# knapsack_01 function being called on the `knapsack` instance which does the following:
knapsack_01(knapsack, item_list)
#   `item_list.sort(key = attrgetter(value'), reverse = True)`
# 1. takes the `item_list`` (starting out as the empty list `initial_knapsack_list`) and 
#    sorts it in reverse order based on the value which is gotten by the `attrgetter` function from the `operator` module
#   `remaining = knapsack.max_weight`
# 2. stores the `max_weight` attribute of `knapsack` (instance of `Knapsack`)  in the `remaining` variable
# 3. for loop iterates over each item in the `item_list`, which stores all the instances of the `Item` class.
#   meanwhile, the weight of each item is subtracted from `remaining`

print('Objects in knapsack')

# a counter for the next for loop?
i = 1

# declare variables for total weight and value
sum_weight = 0 
sum_value = 0

for item in knapsack.item_list:
    sum_weight += item.weight
    sum_value += item.value
    print(f'{i}: weight {item.weight}, value {item.value}')
    i += 1


# what is this for? 
print()

print(f'Total weight of items in knapsack: {sum_weight}')
print(f'Total value of items in knapsack: {sum_value}')
