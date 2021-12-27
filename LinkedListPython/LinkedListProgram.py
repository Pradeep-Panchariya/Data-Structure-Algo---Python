#Traverse the linked List
#Time complexity : O(N)

#define the Node class
#It is as a container which will hold the data and ref of the any new node
#Represantation of this class

""" ________________
    |data|nextNode|
    ----------------
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

#define the linked list class for linking the newly node and do basic operations.

class LinkedList:

    def __init__(self):
        self.head = None
        self.increment_node = 0

    #Traverse the Linked List and print the element.
    def traverse(self):

        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.nextNode

    # Adding the item at the beginning O(1)
    def add_begin(self, data):
        self.increment_node += 1
        new_node = Node(data) #Creating the new node
        new_node.nextNode = self.head #Pointing the head pointer to new node
        self.head = new_node# Poiniing the new node pointer to the head node

    def add_end(self, data):
        self.increment_node += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nextNode is not None:
                n = n.nextNode
            n.nextNode = new_node

    def add_after(self,data, x):
         n = self.head
         while n is not None:
             if n.data == x:
                 break
             n = n.nextNode
         if n is None:
            print('X is not present',x)
         else:
            new_node = Node(data)
            new_node.nextNode = n.nextNode
            n.nextNode = new_node

    def add_before(self,data, x):
         if self.head is None:
             print("Linked list is empty")
         if self.head.data ==x:
             self.add_begin(data)
         else:

             n = self.head
             while n is not None:
                 if n.nextNode.data==x:
                     break
                 n = n.nextNode
             if n is None:
                 print("Not present")
             else:
                 new_node = Node(data)
                 new_node.nextNode = n.nextNode
                 n.nextNode = new_node


if __name__ == '__main__':
    L1  = LinkedList()
    L1.traverse()
    L1.add_begin(34)
    L1.add_begin(43)
    L1.add_end(34)
    L1.add_end(555)
    L1.add_after(12,34)
    L1.add_before(66,34)
    L1.add_after(7,555)
    L1.traverse()
