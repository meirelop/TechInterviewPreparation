# Stacks

LIFO: Last-In, First-Out

## Complexity
O(1) to pop the last element of a Python list, and O(N) to pop an arbitrary element (since the whole rest of the list has to be shifted).


```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

    def size(self):
        return len(self.items)
```
