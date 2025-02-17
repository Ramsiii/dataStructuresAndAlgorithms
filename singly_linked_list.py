
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    # head and tail are not parameters because instances do not require them as arguments
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, new_node):
        
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

# insert a new node following the node with target_data, e.g. my_node = Node('target') 
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

# insert a new node as the head 
    def ins_as_head(self,new_node):
        
        # if the list is empty:
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        # if list not empty, insert before head 
        else:
            new_node.next = self.head
            self.head = new_node

# delete a node based on the data attribute of the Node class
    def del_node(self, target_data):
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

# print all nodes with pointers  
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   

# delete head node
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
        
# check if Linked List is empty

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    
    l_list = LinkedList()
    print('Linked List:')
    l_list.print_list()
    node14 = Node('n')
    node16 = Node('o')
    node17 = Node('p')
    node18 = Node('q')

    print("\nAdd two nodes to empty LL.")
    l_list.add_node(node14)    
    l_list.add_node(node16)

    print('Linked List:')
    l_list.print_list()
    
    print("\ntest deletion of tail node")
    l_list.del_tail_node()
    print('Linked List:')
    l_list.print_list()

    print("Add node16 'o' back in. Add two more nodes:")
    l_list.add_node(node16)
    l_list.add_node(node17)
    l_list.add_node(node18)    
    
    print('Linked List:')
    l_list.print_list()
    node15 = Node('ñ')
    
    print("\ntest insertion of node15 'ñ' after existing data 'n':")
    l_list.ins_node('n', node15)
    
    print('Linked List:')
    l_list.print_list()
    
    
    node13 = Node('m')
    print("\ntest insertion of new node13 'm' as head")
    l_list.ins_as_head(node13)    

    print('Linked List:')
    l_list.print_list()
    
    print("\ntest deletion of data 'ñ' from LL") 
    l_list.del_node('ñ')
    print('Linked List:')
    l_list.print_list()

    print("\ntest deletion of data 'a' not in LL")
    l_list.del_node('a')
    print('Linked List:')
    l_list.print_list()
    
    print("\ntest deletion of data 'm' at head")
    l_list.del_node('m')
    print('Linked List:')
    l_list.print_list()
    
    print("\ntest deletion of data 'q' at tail")
    l_list.del_node('q')
    print('Linked List:')
    l_list.print_list()
    
    print("\ntest deletion of head node")
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
    