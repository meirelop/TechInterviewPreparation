# Stacks

FIFO: First-In, First-Out

## Complexity
Enqueue - 𝑂(1);
Dequeue - 𝑂(1);
Searching - 𝑂(𝑛);
Remove from tail - 𝑂(𝑛);


```python
class Queue:

    #Constructor
    def __init__(self):
        self.queue = list()
        self.maxSize = 8
        self.head = 0
        self.tail = 0

    #Adding elements
    def enqueue(self,data):
        #Checking if the queue is full
        if self.size() >= self.maxSize:
            return ("Queue Full")
        self.queue.append(data)
        self.tail += 1
        return True     

    #Deleting elements 
    def dequeue(self):
        #Checking if the queue is empty
        if self.size() <= 0:
            self.resetQueue()
            return ("Queue Empty") 
        data = self.queue[self.head]
        self.head+=1
        return data
                
    #Calculate size
    def size(self):
        return self.tail - self.head
    
    #Reset queue
    def resetQueue(self):
        self.tail = 0
        self.head = 0
        self.queue = list()
    
q = Queue()
```
