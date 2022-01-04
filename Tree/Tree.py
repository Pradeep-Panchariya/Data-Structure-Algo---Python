"""
@Author : Pradeep panchariya
@Email : panchariya11@gmail.com
"""

#Implementing the all method of Tree data structure because it is effcient compare
# to Linkedlist and List.
#Define the BST : Binary Search Tree class
"""
              ------------------------------------
              |leftChild | Key/data | rightChild |
             --------------------------------------
"""
class BST :
    ##it has three members in the node Leftchild, Key/data, Rightchild
    def __init__(self, key):
        self.key = key
        self.left_child = None
        self.right_child = None

    #insert the new key in the tree .
    def insert(self, key):
        #if the tree is empty
        #here self is also treat as a ROOT NODE. Object of the Tree when it first initialize
        if self.key is None: # None | None | None
            self.key = key
            return # exit the program

        #to deal with duplicate node
        if self.key==key:
            return# exit the method
        # if the tree is not empty it has key in the root node
        #then we have two choice if the newly data is less than or greater than the root node Key
        #if the key is less than tha root key then it will go to the left child
        if self.key > key :
            #now we have two condition if the root node left child is None or it has child .
            # if the child of the root node is not none
            if self.left_child is not None: # self.left_child
                #recursively check and go till the leaf node
                self.left_child.insert(key)
            # if the left child of the root node is none
            else:
                self.left_child = BST(key)

        else:
            #it is same for the right child : if the key is greater than the root Key
            # if the right child is not empty then search recursively till the leaf node
            if self.right_child is not None: # self.right_child also valid
                self.right_child.insert(key)
            #if the root node , right child is empty or Nonr or Null.
            else:
                self.right_child = BST(key)

# executing the program
if __name__ == '__main__':
    root = BST(10)
    keys = [2,5,12,57,7,6]
    for key in keys:
        root.insert(key)
