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
    # Avg case : O(LogN), worst cast : O(N) (If tree is imbalanced)
    def insert(self, data):
        #if the tree is empty
        #here self is also treat as a ROOT NODE. Object of the Tree when it first initialize
        if self.key is None: # None | None | None
            self.key = key
            return # exit the program

        #to deal with duplicate node
        if self.key==data:
            return# exit the method
        # if the tree is not empty it has key in the root node
        #then we have two choice if the newly data is less than or greater than the root node Key
        #if the data is less than tha root key then it will go to the left child
        if self.key > data :
            #now we have two condition if the root node left child is None or it has child .
            # if the child of the root node is not none
            if self.left_child is not None: # self.left_child
                #recursively check and go till the leaf node
                self.left_child.insert(data)
            # if the left child of the root node is none
            else:
                self.left_child = BST(data)

        else:
            #it is same for the right child : if the data is greater than the root Key
            # if the right child is not empty then search recursively till the leaf node
            if self.right_child is not None: # self.right_child also valid
                self.right_child.insert(data)
            #if the root node , right child is empty or Nonr or Null.
            else:
                self.right_child = BST(data)


    #Search the item in the Tree, if the given item is present or not
    # Avg case : O(LogN), worst cast : O(N) (If tree is imbalanced)
    def search(self, data):
        # if the key is present return 1 else return -1
        if self.key == data:
            print(data," is present")
            return
        # if data is greater than key then search in the right subtree
        if data > self.key:
            # if the left child is empty
            if not self.right_child:
                print(data," is not present")
                return
            else:
                self.right_child.search(data)
        # if datais smaller than key then search in the left subtree
        else:
            if not self.left_child:
                print(data," is not present")
                return
            else:
                self.left_child.search(data)

    #Pre Order traversal : Root, Left, Right
    def preorder_traversal(self):
        print(self.key,end=', ')
        if self.left_child:
            self.left_child.preorder_traversal()
        if self.right_child:
            self.right_child.preorder_traversal()

    #In order traversal : left, root, right
    def inorder_traversal(self):
        if self.left_child:
            self.left_child.inorder_traversal()
        print(self.key, end = ', ')
        if self.right_child:
            self.right_child.inorder_traversal()

    #Post order : Left, right, root
    def postorder_traversal(self):
        #traverse until we do not find the left child empty
        if self.left_child:
            self.left_child.postorder_traversal()
        #taverse till the right child is not empty.
        if self.right_child:
            self.right_child.postorder_traversal()
        print(self.key, end=', ')

    #find the max item in the tree : go leaf node of the right child
    def find_max(self):
        if self.right_child:
            self.right_child.find_max()
        else:
            print(self.key)

    #find the minimum item in the tree; : go to the leaf node of the left child
    def find_min(self):
        if self.left_child is not None: # self.left_child
            self.left_child.find_min()
        #if we reached the leaf node then get the key and print it
        else:
            print(self.key)

    #delte the node
    def delete(self, data,first_root_node):
        #check if the tree is empty or not
        if self.key is None:
            print("Tree is empty")
            return
        #search if the search item is present in the tree or not
          #if the searching data is smaller than current key of node search in left Subtree
        if self.key > data :
            # check whether left subtree is empty or not
            if self.left_child: # self.left_child is not None
                #storing the return value to the self.left_child object
                self.left_child = self.left_child.delete(data,first_root_node)
            else:
                print("Data is not present in Tree")
        #if the searching data is greater than the root key go to right child
        elif self.key < data:
            #check whether right subtree is empty or not
            if self.right_child:
                #storing or referencing the return value of recursive fun to the right children
                self.right_child = self.right_child.delete(data,first_root_node)
            else:
                print("Data is not present in Tree")

        #if data is found then process following steps
        else:
            #it is valid for if the root not has one child or 0 child
            #check if the left child is None for the found data : which gonna to delete
            if self.left_child is None:
                #store the address of current right child  node : delete node
                temp = self.right_child
                if first_root_node==data:
                    self.key = temp.key
                    self.left_child = temp.left_child
                    self.right_child = temp.right_child
                    temp = None
                    return
                self = None # deleting the node
                return temp #connect the right child reference to the root node
            elif self.right_child is None:
                temp = self.left_child
                if first_root_node == data:
                    self.key = temp.key
                    self.left_child = temp.left_child
                    self.right_child = temp.right_child
                    temp = None
                    return
                self = None
                return temp
            #if the root has left and right child : present both child
            #first replace the root node with smaller value of it left child
            node = self.right_child
            while node.left_child:
                node = node.left_child
            #replace root node with smallest value
            self.key = node.key
            self.right_child = self.right_child.delete(node.key,first_root_node)
        return self

#Interview Question
#Compare if two tree are equa or not
def compare_tree(node1, node2):
    if node1 is None or node2 is None:
        return node1==node2
    if node1.key is not node2.key:
        return False
    return compare_tree(node1.left_child,node2.left_child) and compare_tree(node1.right_child,node2.right_child)

#counting the total number of nodes present in tree
def count_node(node):
    if node is None:
        return 0
    return 1+count_node(node.left_child)+count_node(node.right_child)



# executing the program
if __name__ == '__main__':
    root = BST(10)
    keys = [2,5,12,57,7,1]
    # keys=[2]
    for key in keys:
        root.insert(key)#behind the underhood : BST.insert(root,key) = root.insert(key)
        # BST.insert(root,key)
    print("Search the item 2 in the tree:")
    root.search(2)
    print()
    print("PreOrder Traversal: ")
    root.preorder_traversal()
    print("\nInOrder Traversal:")
    root.inorder_traversal()
    print("\nPostOrder Traversal:")
    root.postorder_traversal()
    print("\n\nMaximum item in the tree:",end=" ")
    root.find_max()
    print("\nMinimum item in the tree:",end=" ")
    root.find_min()
    #delete the node
    #if the count of node is more than 1 then perform delete operation
    if count_node(root)>1:
        root.delete(10,root.key)#Root.key : check if there is only one node and it has one or two child.
    #Oterwise print the msg that there are only onde node, we will not delete it.
    else:
        print("Can not delete root node, present only one item in tree")
    print()
    root.inorder_traversal()

    #comparing two trees
    node1 = BST(10)
    keys = [2,10,4,5,7,8]
    for key in keys:
        node1.insert(key)
    node2 = BST(10)
    keys = [2,10,44,5,7,8]
    for key in keys:
        node2.insert(key)
    print("\ntwo tree is equal or not? ",compare_tree(node1,node2))
