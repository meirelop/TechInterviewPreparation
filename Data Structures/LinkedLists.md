# Linked List

## Definition
A linked list consists of nodes. Each node consists of a value and a pointer to another node.
Essentially, linked list is a chain of values connected with pointers.


## Complexity
Add item:       Linked list - O(1), Array - O(1)
Delete item:    Linked list - O(1), Array - O(n), Array will shift to one postition all elemenents, if we do pop(0)
Access item:    Linked list - O(n), Array - O(1)

## Usage
When we need to only add and delete.
Ex: Queue of people waiting in line for popcorn


```python
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start_node = None      


    def traverse_list(self):
    if self.start_node is None:
        print("List has no element")
        return
    else:
        n = self.start_node
        while n is not None:
            print(n.item , " ")
            n = n.next  

    def insert_at_start(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node= new_node


    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n= n.next
        n.next = new_node;


    def insert_after_item(self, x, data):
        n = self.start_node
        print(n.next)
        while n is not None:
            if n.item == x:
                break
            n = n.next
        if n is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List has no element")
            return

        if x == self.start_node.item:
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node = new_node
            return

        n = self.start_node
        print(n.next)
        while n.next is not None:
            if n.next.item == x:
                break
            n = n.next
        if n.next is None:
            print("item not in the list")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


    def insert_at_index (self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.next = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.next
            i = i+1
        if n is None:
            print("Index out of bound")
        else: 
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node


    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count + 1
            n = n.next
        return count


    def search_item(self, x):
        if self.start_node is None:
            print("List has no elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item found")
                return True
            n = n.next
        print("item not found")
        return False


    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        self.start_node = self.start_node.next


    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return

        n = self.start_node
        while n.next.next is not None:
            n = n.next
        n.next = None


    def reverse_linkedlist(self):
        prev = None
        n = self.start_node
        while n is not None:
            _next = n.next
            n.next = prev
            prev = n
            n = _next
        self.start_node = prev

```


