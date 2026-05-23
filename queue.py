

class Queue(): #First in First Out 
    def __init__(self,size):
        self.size = size
        self.list = []
        self.available = size
        
    def enqueue(self,item):
        self.item = item
        if self.available > 0:
            self.list.append(item)
            self.available = self.available - 1
        else:
            print("Queue Overflow")

    def dequeue(self):
        if len(self.list) > 0:
            self.list.pop(0)
            self.available = self.available + 1

        else:
            print("Queue underflow")
        
    def display(self):
        for i in self.list:
            print(i)

    
object = Queue(size = 5)

object.enqueue(1)
object.enqueue(5)
object.enqueue(10)
object.dequeue()
object.display()