expression = input("Please input in an expression: ")
from Stacks import Stack
object = Stack(size = 30)

open_brackets = ["(","[","{"]
close_brackets = [")","]","}"]

for i in expression:
    print(object.list)
    if i in open_brackets:
        object.push(item = i )
    
    elif i in close_brackets:
        b = object.list[-1]
        b_i = open_brackets.index(b)
        if close_brackets.index(i) == b_i:
            object.pop()
     
        else:
            break

if len(object.list) > 0:
    print("Brackets not matched and expression is not balanced")
else:
    print("Brackets sorted and expression is balanced")



