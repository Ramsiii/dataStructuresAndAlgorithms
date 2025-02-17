
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    
    """
    LinkedList class
    
    Methods:
    - append(self, new_node): adds a new node to tail of LL, 
        either to an empty LL as head and tail or to the end as tail
    - ins_node(self, target_data, new_node): inserts a new node following the node with target_data
    - push(self,new_node): inserts a new node as the head aka prepend()
    - remove(self, target_data): removes the first instance of a node based on the data attribute of the Node class
    - del_head_node(self): deletes head node (without returning it) and reassigns head to next node or None (if LL then empty)
    - del_tail_node(self): deletes tail node (without returning it) and reassigns tail to previous node or None (if LL then empty)
    - is_empty(self): checks if LL is empty, returns True if empty, False if not
    - print_list(self): prints all nodes with pointers as " -> "
    """
    
# head and tail are not parameters because instances do not require them as arguments
    def __init__(self):
        self.head = None
        self.tail = None

# adds a new node to end of LL, either to an empty list or to the end
    def append(self, new_node):
        
        # if the list is empty:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        # if there are one or more nodes. 
        # new_node is set to point at None in the Node class with the .next attribute
        else:
            # point tail node at new_node (befor this action: self.tail.next is None (empty)
            self.tail.next = new_node
            # point tail at new_node
            self.tail = new_node
            new_node.next = None

# inserts a new node following the node with target_data, e.g. my_node = Node('target') 
    def ins_node(self, target_data, new_node):
        current = self.head
        
        while current is not None:
            if current.data == target_data:
                
                # if target_data node is the tail, simply append   
                if current is self.tail:
                    self.tail.next = new_node
                    self.tail = new_node
                    new_node.next = None
                else:
                    # Insert between current and next node
                    new_node.next = current.next
                    current.next = new_node
                return  # Exit after inserting
            # iterate to next node
            current = current.next
    
        # If target_data wasn't found, print this:
        print(f"Node with data '{target_data}' not found")         

# inserts a new node as the head aka prepend()
    def push(self,new_node):
        
        # if the list is empty:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        # if list not empty, insert before head 
        else:
            new_node.next = self.head
            self.head = new_node

# removes the first instance of a node based on the data attribute of the Node class
    def remove(self, target_data):
        current = self.head
        previous = None
    
        while current is not None:
            if current.data == target_data:
                if previous:  # If there's a previous node
                    if current.next is not None:
                        previous.next = current.next  # Point previous -> next node
                    else:
                        previous.next = None
                else:
                    self.head = current.next
                return
            previous = current
            current = current.next
                    
        # If target_data wasn't found, print this:
        print(f"Node with data '{target_data}' not found")

# deletes head node
    def del_head_node(self):
        # if there is more than one node:
        if self.head is not None and self.head.next is not None:
            self.head = self.head.next
        # if there is only one node:
        elif self.head is not None and self.head.next is None:
            self.head = None
            self.tail = None
        else:
            print(f'This linked list is empty.')

# delete tail node 
    def del_tail_node(self):
        
        if self.head is None:
            print(f'This linked list is empty.')
            return
        
        # if there is only one node:
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return
        # multiple nodes:
        
        current = self.head

        while current.next is not self.tail:
            current = current.next                    

        current.next = None
        self.tail = current
        
# checks if LL is empty

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

# prints all nodes with pointers as " -> "
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")           
        
if __name__ == '__main__':
    
    l_list = LinkedList()
    print('Linked List:')
    l_list.print_list()
    node14 = Node('n')
    node16 = Node('o')
    node17 = Node('p')
    node18 = Node('q')

    print("\nAppend two nodes to empty LL.")
    l_list.append(node14)    
    l_list.append(node16)

    print('Linked List:')
    l_list.print_list()
    
    print("\ntest deletion of tail node")
    l_list.del_tail_node()
    print('Linked List:')
    l_list.print_list()

    print("Append node16 'o' back in. Append two more nodes:")
    l_list.append(node16)
    l_list.append(node17)
    l_list.append(node18)    
    
    print('Linked List:')
    l_list.print_list()
    node15 = Node('ñ')
    
    print("\ntest insertion of node15 'ñ' after existing data 'n':")
    l_list.ins_node('n', node15)
    
    print('Linked List:')
    l_list.print_list()
    
    
    node13 = Node('m')
    print("\ntest push(): insertion of new node13 'm' as head")
    l_list.push(node13)    

    print('Linked List:')
    l_list.print_list()
    
    print("\ntest remove() method, i.e. deletion of data 'ñ' from LL") 
    l_list.remove('ñ')
    print('Linked List:')
    l_list.print_list()

    print("\ntest remove() method, i.e. deletion of data 'a' not in LL")
    l_list.remove('a')
    print('Linked List:')
    l_list.print_list()
    
    print("\ntest remove() method, i.e. deletion of data 'm' at head")
    l_list.remove('m')
    print('Linked List:')
    l_list.print_list()
    
    print("\ntest remove() method, i.e. deletion of data 'q' at tail")
    l_list.remove('q')
    print('Linked List:')
    l_list.print_list()
    
    print("\ntest remove() method, i.e. deletion of head node")
    l_list.del_head_node()
    print('Linked List:')
    l_list.print_list()
        
    print("\ntest is_empty method with non-empty linked list")
    print(f"is l_list empty? {l_list.is_empty()}")

    
    # LL2 --------------------
    
    print("\nNew instance of LL class LL2.")
    l_list2 = LinkedList()
    print("\ntest deletion of head node from empty LL2")
    l_list2.del_head_node()

    print('\nEmpty Linked List 2:')
    l_list2.print_list()

    print('Test del_tail_node funciton:')
    l_list2.del_tail_node()
    
    print("\ntest is_empty method with empty linked list")
    print(f"is l_list2 empty? {l_list2.is_empty()}")
    