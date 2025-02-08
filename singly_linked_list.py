
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
        
        # if there are one or more nodes. 
        # new_node is set to point at None in the Node class
        else:
            # point tail node at new_node self.tail.next == <last_node>
            self.tail.next = new_node
            # point tail at new_node
            self.tail = new_node
            
    def ins_node(self, target_data, new_node):
        current = self.head
        
        while current is not None:
            if current.data == target_data: 
                # if target_data node is the tail, simply append   
                if current is self.tail:
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    # Insert between current and next node
                    new_node.next = current.next
                    current.next = new_node
                return  # Exit after inserting
            # iterate to next node
            current = current.next
    
        # If target_data wasn't found, print this:
        print(f"Node with data '{target_data}' not found")         
        
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")   
    
if __name__ == '__main__':
    
    l_list = LinkedList()
    node14 = Node('n')
    node16 = Node('o')
    node17 = Node('p')

    l_list.add_node(node14)    
    l_list.add_node(node16)
    l_list.add_node(node17)
    
    node15 = Node('ñ')
    
    l_list.ins_node('n', node15)
    
    l_list.print_list()
    