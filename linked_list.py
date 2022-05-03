from node import Node


class LinkedList:

    def __init__(self) -> None:
        """Instantiates the head node"""
        self.head = None
    
    def insert_node(self, value):
        """Inserts a new node in 3 different ways:

        (1) If the head node is empty, create the new node at the head node.

        (2) INSERT AT BEGINNING: If the value in the head node is greater than 
        the value of the node being inserted, then point the pointer to head. 
        The new node will be the head node.

        (3) INSERT IN BETWEEN A "PREVIOUS" NODE AND A "CURRENT" NODE:
        If the value of the node to be inserted is greater than the current
        value and we are not at the end of linked list, move both the pointers 
        for previous and current node to the right, so previous becomes current,
        and current becomes next.
        - When the condition is false, exit out of while loop. Reassign the pointer
        for the new node to point to current, and reassign the pointer for the
        previous node to new node.
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif self.head.value >= value:
            new_node.next = self.head
            self.head = new_node
        else:
            previous = self.head
            current = self.head.next
            # current is not None means not at the end of the linked list
            while (current is not None) and (value > current.value):
                previous = current
                current = current.next
        
            new_node.next = current
            previous.next = new_node
    
    def print_list_items(self):
        """Traverses a linked list to print its element."""
        if self.head is None:
            print('Empty')
        else:
            current = self.head      # current node
            while current is not None:
                print(current.value, end=' ')
                current = current.next
            print()

    def count_nodes(self):
        """Count the nodes of a linked list iteratively"""
        counter = 0
        current = self.head
        while current is not None:
            counter += 1
            current = current.next
        return counter




my_linked_list = LinkedList()
my_linked_list.insert_node("Python")
my_linked_list.insert_node("World")
my_linked_list.insert_node("Hello")
my_linked_list.insert_node("Code")


print(my_linked_list.print_list_items())
print(my_linked_list.count_nodes())

