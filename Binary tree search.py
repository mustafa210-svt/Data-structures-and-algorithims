#Binary tree search
#------------------
#Binary tree can only have 2 children max 

#If number is smaller it goes on the left
#If number is larger it goes on the right


class Tree():
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def preorder(self):
        print(self.data)
        if self.leftchild != None:
            self.leftchild.preorder()
        
        if self.rightchild != None:
            self.rightchild.preorder()
    
    def inorder(self):
        if self.leftchild != None:
            self.leftchild.inorder()

        print(self.data)

        if self.rightchild != None:
            self.rightchild.preorder()

    def postorder(self):
        if self.leftchild != None:
            self.leftchild.postorder()
        
        if self.rightchild != None:
            self.rightchild.postorder()
        
        print(self.data)

    def search(self,num):
        if self.data == num:
            return "Search succesful"
        
        elif num > self.data and self.rightchild != None :
            return self.rightchild.search(num)
        

        elif num < self.data and self.leftchild != None  :
            return self.leftchild.search(num)
        
        return "Search unsuccesful"

    def insert(self,value):

        if value <= self.data:
            if self.leftchild != None:
                self.leftchild.insert(value)
            else:
                self.leftchild = Tree(value)
        
        elif value > self.data: 
            if self.rightchild != None:
                self.rightchild.insert(value)
            else:
                self.rightchild = Tree(value)
        


        
        

  
#root and children
root = Tree(50)
root.leftchild = Tree(20)
root.rightchild = Tree(60)
#leafs
root.leftchild.leftchild = Tree(7)
root.leftchild.rightchild = Tree(21)
root.rightchild.leftchild = Tree(56)
root.rightchild.rightchild = Tree(80)

num = int(input("Input a number you are looking for in the tree"))

print(root.search(num))
root.insert(40)
print(root.preorder())


