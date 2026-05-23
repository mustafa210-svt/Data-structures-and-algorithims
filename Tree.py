#Tree data structure (non linear)
#A tree with a max of 2 children is a binary tree

#pre = root left right
#in = left root right
#post = left right root 
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
        
         
        

        
    

        

#root and children
root = Tree(10)
root.leftchild = Tree(20)
root.rightchild = Tree(5)
#leafs
root.leftchild.leftchild = Tree(7)
root.leftchild.rightchild = Tree(3)
root.rightchild.leftchild = Tree(6)
root.rightchild.rightchild = Tree(50)

print('preorder sequence' )
root.preorder()
print('inorder sequence')
root.inorder()
print('post order sequence')
root.postorder()

