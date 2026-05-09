class Stack:
    def __init__(self,size):
        self.list = []
        self.size = size    
  

    def push(self,item):
        self.item = item
        if len(self.list)<= self.size:
            self.list.append(item)
        else:
            print("stack overflow")
        
    def pop(self):
        if len(self.list) > 0:
            self.list.pop(-1)

        else:
            print("Stack underflow")
    
    def display(self):
        print(self.list)
        
        
object = Stack(size= 5)

object.pop()
object.display()
